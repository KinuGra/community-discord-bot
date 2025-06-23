from db.connection import get_connection
import mysql.connector

def insert_progress(author_id: int, title: str, detail: str):
    try:
        conn = get_connection() # 接続取得
        cursor = conn.cursor()

        sql = """
        INSERT INTO progress_logs (author_id, progress_title, progress_detail)
        VALUES (%s, %s, %s)
        """
        val = (author_id, title, detail)
        cursor.execute(sql, val)
        conn.commit()

    except mysql.connector.Error as err:
        print("INSERTエラー:", err)
        raise

    finally:
        if 'cursor' in locals(): cursor.close()
        if 'conn' in locals(): conn.close()