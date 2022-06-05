from flask import Flask, render_template
import sqlite3


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/home')
def home_page():
    
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    
    return render_template('home.html', posts=posts)

@app.route('/about')
def about_page():
    return render_template('about.html')