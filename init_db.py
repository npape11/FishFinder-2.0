import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

conn = psycopg2.connect(
        host=os.getenv('HOST'),
        database=os.getenv('DB'),
        user=os.getenv('DB_USERNAME'),
        password=os.getenv('DB_PASSWORD'))

cur = conn.cursor()

with open('schema.sql') as f:
    cur.execute(f.read())

conn.commit()

cur.close()
conn.close()

