# db/connection.py
import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv

load_dotenv()  # .env から環境変数を読み込む

def get_connection():
    try:
        conn = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
        return conn  # 接続成功時のみ返す

    except Error as err:
        print("データベース接続エラー:")
        print(err)
        raise  # 呼び出し元に通知する（exceptで握りつぶさない）
