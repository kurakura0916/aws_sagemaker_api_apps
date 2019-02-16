## 開発環境

### 開発環境のライブラリ
```
# version確認
$ python --version
Python 3.6.3

# venv
$ python -m venv env

# activate
. env/bin/activate

# 必要なライブラリのインストール
$ pip install -r ./config/requirements.txt
```


## 環境構築

### SageMakerのエンドポイントの作成

```
./script/create_endpoint.sh
```

### cloudformationによるAPI Gateway / lambdaの環境構築

```
./script/cloudformation/create_stack.sh
```


- いらなくなったformationとエンドポイントを削除する

```
./script/cloudformation/delete_stack.sh
```

```
./script/sagemaker/delete_endpoint.sh
```

### APIの動作確認

```
curl -d '{"test1":1, "test2":1, "test3":1, "test4":1}' \
-H 'x-api-key:your-api-key' \
https://your-api-url
```


## アプリケーションの起動

```
python apps.py
```


- 出力結果
```
/Users/sagemaker-api/apps.py
 * Serving Flask app "apps" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 162-239-879
```

1. ブラウザを開いて`http://0.0.0.0:5000/`にアクセスする。
2. 入力フォームに値を入れ`submit`ボタンを押下する。
3. 分類結果が出力されれば無事完了。
