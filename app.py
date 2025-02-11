from flask import Flask, render_template
from dotenv import load_dotenv
import psycopg2
import os

app = Flask(__name__)

load_dotenv()

def get_db_connection():        
    conn = psycopg2.connect(
            host=os.getenv('HOST'),
            database=os.getenv('DB'),
            user=os.getenv('DB_USERNAME'),
            password=os.getenv('DB_PASSWORD'))
    cur = conn.cursor()
    print('good')
    return cur

@app.route('/')
def index():
    cur = get_db_connection()
    tst = cur.execute('SELECT * FROM users')
    cur.close()
    return tst
