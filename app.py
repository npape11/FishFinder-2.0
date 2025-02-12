from flask import Flask, render_template, request, redirect, url_for
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
    return conn

@app.route('/')
def index():
    
    conn = get_db_connection()
    cur = conn.cursor()

    # Select all products from the table
    cur.execute("SELECT * FROM users")

    # Fetch the data
    data = cur.fetchall()

    # close the cursor and connection
    cur.close()
    conn.close()

    return render_template('index.html', data=data)

@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO users (username, email, password) VALUES (%s, %s, %s)', (username, email, password))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('index'))

    return render_template('create.html')

if __name__ == '__main__': 
    app.run(debug=True)
