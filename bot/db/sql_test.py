import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv() # .envファイルを読み込む

# MySQLサーバーへの接続情報
conn = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
)

# 接続確認
if conn.is_connected():
    print("MySQLサーバーに接続成功！")