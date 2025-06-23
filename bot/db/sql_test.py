import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv() # .envファイルを読み込む

# MySQLサーバーへの接続情報
conn = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    # database="sample_db"
)

# 接続確認
if conn.is_connected():
    print("MySQLサーバーに接続成功！")

cursor = conn.cursor()

# データベース作成
cursor.execute("CREATE DATABASE IF NOT EXISTS sample_db")
print("データベース（sample_db）は作成済みまたは作成完了")

# テーブル作成
cursor.execute("USE sample_db")
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100)
)
""")
print("テーブル（users）は作成済みまたは作成完了")

# CRUD（C）
# データを追加する
sql = "INSERT INTO users (name, email) VALUES (%s, %s)"
val = ("山田 太郎", "taro@example.com")
cursor.execute(sql, val) # SQL実行
conn.commit() # 変更保存
"""複数のレコードを追加する
val_list = [
    ("佐藤 花子", "hanako@example.com"),
    ("鈴木 次郎", "jiro@example.com")
]

cursor.executemany(sql, val_list)
conn.commit()
"""

# CRUD（R）
cursor.execute("SELECT * FROM users") # SELECT文で全データ取得
print("登録ユーザー一覧")
for row in cursor:
    print(row)
"""
cursor.execute("SELECT * FROM users WHERE name = %s", ("山田 太郎",))
for row in cursor:
    print(row)
"""

# CRUD（U）
sql = "UPDATE users SET email = %s WHERE name = %s" #! WHEREを忘れると全ての行が書き換えられる
val = ("yamada@example.com", "山田 太郎")
cursor.execute(sql, val)
conn.commit()
print(f"{cursor.rowcount} 件のデータを更新しました")

sql = "UPDATE users SET name = %s, email = %s WHERE id = %s"
val = ("鈴木 正成", "new@example.com", 1)
cursor.execute(sql, val)
conn.commit()

# CRUD（D）
sql = "DELETE FROM users WHERE name = %s" #! DELETE FROM usersは全削除
val = ("山田 太郎",)
cursor.execute(sql, val)
conn.commit()
print(f"{cursor.rowcount} 件のデータを削除しました")

# DB一覧を表示
cursor.execute("SHOW DATABASES")
print("DB一覧：")
for db in cursor:
    print("-", db[0])
# テーブル一覧を表示
cursor.execute("SHOW TABLES")
print("テーブル一覧：")
for table in cursor:
    print("テーブル：", table[0])

cursor.close()
conn.close()