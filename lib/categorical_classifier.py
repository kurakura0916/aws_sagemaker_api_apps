import os
import requests
import json
import yaml

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
API_KEY_FILE = os.path.join(BASE_DIR, "./api-key/api-gateway.yml")


def categorical_classifier(data: dict):
    """
    :param data={
    "sepal length": ,
    "sepla width" : ,
    "petal length" : ,
    "petal width" :
    }

    :return: category(setosa, )
    """
    with open(API_KEY_FILE, mode="r") as file:
        header = yaml.load(file)

    url = 'https://tf6ab4hll1.execute-api.ap-northeast-1.amazonaws.com/dev/SageMaker-API'

    response = requests.post(url, headers=header, data=json.dumps(data)).json()
    print(response)
    return response

