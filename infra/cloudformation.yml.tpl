---
# define include macro
{% macro include(file) %}{% include(file) %}{% endmacro %}

AWSTemplateFormatVersion: 2010-09-09
Description: API GateWay environment
# =======set parameters======== #
Parameters:
  FunctionName:
    Type: String
    Description: dev-api
    Default: "SageMaker-API"
  Runtime:
    Description: Language of scripts
    Type: String
    Default: python3.6

Resources:
  # =======IAM======== #
  InvokeSageMakerLambdaRole:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Version: "2012-10-17"
        Statement:
          - Effect: Allow
            Principal:
              Service:
                - lambda.amazonaws.com
            Action:
              - sts:AssumeRole
      ManagedPolicyArns:
        - arn:aws:iam::aws:policy/AWSLambdaFullAccess
        - arn:aws:iam::aws:policy/AmazonSageMakerFullAccess
      Path: "/service-role/"

  # =======lambda======== #
  InvokeSageMakerLambda:
    Type: AWS::Lambda::Function
    Properties:
      Code:
        ZipFile: !Sub |
          {{ include('./lambda_script/invoke_sagemaker/lambda_function.py')|indent(10) }}
      Description: "Sagemaker API Invoke"
      FunctionName: !Sub "${FunctionName}"
      Handler: index.lambda_handler
      MemorySize: 128
      Role: !GetAtt InvokeSageMakerLambdaRole.Arn
      Runtime: !Ref Runtime
      Timeout: 15

  # =======API Gateway======== #
  SageMakerApi:
    Type: AWS::ApiGateway::RestApi
    Properties:
      Name: "SageMakerApi"
  Resource:
    Type: AWS::ApiGateway::Resource
    Properties:
      RestApiId: !Ref SageMakerApi
      ParentId: !GetAtt SageMakerApi.RootResourceId
      PathPart: !Sub "${FunctionName}"
    DependsOn: "InvokeSageMakerLambda"
  LambdaPermission:
    Type: AWS::Lambda::Permission
    Properties:
      FunctionName: !Sub "${FunctionName}"
      Action: "lambda:InvokeFunction"
      Principal: "apigateway.amazonaws.com"
    DependsOn: "InvokeSageMakerLambda"
  ResourceMethod:
    Type: AWS::ApiGateway::Method
    Properties:
      RestApiId: !Ref SageMakerApi
      ResourceId: !Ref Resource
      AuthorizationType: "None"
      HttpMethod: "POST"
      Integration:
        Type: "AWS"
        IntegrationHttpMethod: "POST"
        Uri: !Sub "arn:aws:apigateway:${AWS::Region}:lambda:path/2015-03-31/functions/arn:aws:lambda:${AWS::Region}:${AWS::AccountId}:function:${FunctionName}/invocations"
        IntegrationResponses:
        - StatusCode: 200
      MethodResponses:
      - StatusCode: 200
    DependsOn: "LambdaPermission"

  ApiGatewayDeployment:
    Type: AWS::ApiGateway::Deployment
    DependsOn: "ResourceMethod"
    Properties:
      RestApiId: !Ref SageMakerApi
      StageName: "dev"
