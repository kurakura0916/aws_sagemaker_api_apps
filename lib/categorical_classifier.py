import os
import requests
import json
import yaml

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
API_KEY_FILE = os.path.join(BASE_DIR, "./api-key/api-gateway.yml")
API_URL = 'your_api_url'

def categorical_classifier(data: dict) -> dict:
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

    response = requests.post(API_URL, headers=header, data=json.dumps(data)).json()
    print(response)
    return response
