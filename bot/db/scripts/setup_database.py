import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv() # .envファイルを読み込む

DB_NAME="discord_bot"
TABLE_NAME = "progress_logs"

try:
    # 接続
    conn = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
    )
    cursor = conn.cursor()

    # データベースがなければ作成
    cursor.execute("SHOW DATABASES")
    databases = [db[0] for db in cursor.fetchall()]
    if DB_NAME not in databases:
        cursor.execute(f"CREATE DATABASE {DB_NAME}")
        print(f"データベース `{DB_NAME}` を新規作成しました")
    else:
        print(f"データベース `{DB_NAME}` は既に存在します")

    # DBを使用
    cursor.execute(f"USE {DB_NAME}")

    # テーブルがなければ作成
    cursor.execute("SHOW TABLES")
    tables = [t[0] for t in cursor.fetchall()]
    if TABLE_NAME not in tables:
        cursor.execute(f"""
            CREATE TABLE {TABLE_NAME} (
                id INT AUTO_INCREMENT PRIMARY KEY,
                author_id BIGINT NOT NULL,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                progress_title VARCHAR(100),
                progress_detail TEXT
            )
        """)
        print(f"テーブル `{TABLE_NAME}` を新規作成しました")
    else:
        print(f"テーブル `{TABLE_NAME}` は既に存在します")

except mysql.connector.Error as err:
    print("エラーが発生しました:")
    print(err)

finally:
    # 接続を閉じる
    if 'cursor' in locals(): cursor.close()
    if 'conn' in locals(): conn.close()