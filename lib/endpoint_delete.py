import logging
from boto3.session import Session

from config import Config


class EndPointDelete:
    def __init__(self):
        self.sagemaker_client = Session(profile_name="local").\
            client("sagemaker", region_name="ap-northeast-1")

    def execute(self):
        result_config = self.delete_endpoint_config()
        logging.info(result_config)
        result = self.delete_endpoint()
        logging.info(result)

    def delete_endpoint_config(self):
        result = self.sagemaker_client.delete_endpoint_config(
            EndpointConfigName=Config.endpoint_config_name()
        )
        return result

    def delete_endpoint(self):
        result = self.sagemaker_client.delete_endpoint(
            EndpointName=Config.endpoint_name()
        )
        return result


if __name__ == '__main__':
    EndPointDelete().execute()