from flask import Flask, render_template
import sqlite3
from werkzeug.exceptions import abort


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post


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

@app.route('/post/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)