class Config:

    @staticmethod
    def base_model_name():
        return 'dev-sagemaker-multiclass'

    @staticmethod
    def endpoint_config_name():
        return 'sagemaker-dev-endpoint-config'

    @staticmethod
    def endpoint_name():
        return 'sagemaker-dev-endpoint'
