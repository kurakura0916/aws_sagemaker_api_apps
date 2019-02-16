import logging
import boto3

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.INFO)

ENDPOINT_NAME = "sagemaker-dev-endpoint"


def lambda_handler(event, _context):
    client = boto3.client("sagemaker-runtime", region_name="ap-northeast-1")
    values = list(event.values())

    response = client.invoke_endpoint(
        EndpointName=ENDPOINT_NAME,
        Body='{0}, {1}, {2}, {3}'.format(values[0], values[1], values[2], values[3]),
        ContentType='text/csv',
        Accept='application/json'
    )

    result = response['Body'].read().decode()

    return {
        'statusCode': 200,
        'body': result
    }
