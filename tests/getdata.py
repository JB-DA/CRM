
import sqlite3

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

conn = get_db_connection()
posts = conn.execute('SELECT * FROM posts').fetchall()
conn.close()

for post in posts:
    print( post['title'] )
    print( post['created'] )
