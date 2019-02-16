#!/bin/bash

eval $(aws ecr get-login --region ap-northeast-1 --no-include-email --profile your_profile)



echo "デプロイします。よろしいですか？ [yes/NO]"

read answer

case $answer in
    yes|y)
        DEPLOY_YES=1
        ;;
    *)
        echo "abort"
        exit 1
        ;;
esac


echo "スタックを作成します: sagemaker-app"
# Lambdaの環境を構築する
python ./infra/formation_config_creator.py
aws cloudformation create-stack \
    --stack-name sagemaker-app \
    --template-body file://$PWD/infra/cloudformation.yml \
    --capabilities CAPABILITY_IAM \
    --profile your_profile
