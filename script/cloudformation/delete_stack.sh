#!/bin/bash

echo "sagemaker-appを消します"

aws cloudformation delete-stack \
    --stack-name sagemaker-app \
    --profile your_profile
