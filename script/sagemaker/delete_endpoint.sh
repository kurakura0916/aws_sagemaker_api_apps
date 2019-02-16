#!/bin/bash

echo "エンドポイントを削除します。よろしいですか？ [yes/NO]"

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

echo "エンドポイントを削除します"

python ./lib/endpoint_delete.py
