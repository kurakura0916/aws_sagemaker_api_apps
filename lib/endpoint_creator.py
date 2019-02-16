import logging
from boto3.session import Session

from config import Config


class EndPointCreator:
    def __init__(self):
        self.sagemaker_client = Session(profile_name="your_profile").\
            client("sagemaker", region_name="ap-northeast-1")

    def execute(self):
        model_name = self.get_model_name()
        self.create_end_point_config(model_name)
        self.create_end_point()
        self.wait_end_point(max_iter=120)

    def get_model_name(self):
        model_name = self.sagemaker_client.list_models(
            NameContains=Config.base_model_name(),
            SortOrder='Descending',
            SortBy='CreationTime'
        )["Models"][0]["ModelName"]

        return model_name

    def create_end_point_config(self, model_name):
        self.sagemaker_client.create_endpoint_config(
            EndpointConfigName=Config.endpoint_config_name(),
            ProductionVariants=[
                {
                    'VariantName': 'hoge',
                    'ModelName': model_name,
                    'InitialInstanceCount': 1,
                    'InstanceType': 'ml.m4.xlarge'
                }
            ]
        )

    def create_end_point(self):
        self.sagemaker_client.create_endpoint(
            EndpointName=Config.endpoint_name(),
            EndpointConfigName=Config.endpoint_config_name()
        )

    def wait_end_point(self, max_iter=120):
        waiter = self.sagemaker_client.get_waiter("endpoint_in_service")
        logging.info("polling start")

        waiter.wait(
            EndpointName=Config.endpoint_name(),
            WaiterConfig={"MaxAttempts": max_iter}
        )
        logging.info("polling end")

        res = self.sagemaker_client.describe_endpoint(EndpointName=Config.endpoint_name())
        status = res['EndpointStatus']

        if status != 'InService':
            message = self.sagemaker_client.describe_endpoint(EndpointName=Config.endpoint_name())['FailureReason']
            print('Training failed with the following error: {}'.format(message))
            raise Exception('Endpoint creation did not succeed')

        return status


if __name__ == '__main__':
    EndPointCreator().execute()
