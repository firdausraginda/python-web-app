import sqlite3
from pathlib import Path


connection = sqlite3.connect('database.db')

current_path = Path(__file__).absolute()
path_to_schema = current_path.parent.joinpath('schema.sql')

with open(path_to_schema) as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('First Post', 'Content for the first post')
            )

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Second Post', 'Content for the second post')
            )

connection.commit()
connection.close()