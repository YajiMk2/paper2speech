# Python 3.12-bookwormイメージをベースに使用
FROM python:3.12-bookworm

# 作業ディレクトリを設定
WORKDIR /app

# ホストのrequirements.txtをコンテナにコピー
COPY requirements.txt .

# 必要なPythonライブラリをインストール
RUN pip install --no-cache-dir -r requirements.txt

# ソースコードをコンテナにコピー
COPY src/ /app/src

# Streamlitを使用するためにEXPOSEコマンドでポートを開放
EXPOSE 8501