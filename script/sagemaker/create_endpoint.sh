#!/bin/bash

echo "エンドポイントを作成します。よろしいですか？ [yes/NO]"

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

echo "エンドポイントを作成します"

# sagemakerのエンドポイント設定とエンドポイントの作成
python ./lib/endpoint_creator.py

echo "エンドポイントを作成しました"
