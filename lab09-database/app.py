import sqlite3
import random
from flask import Flask, render_template, request, g

class Poem:
    def __init__(self, title, author, poem_text):
        self.title = title
        self.author = author
        self.poem_text = poem_text

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def index():
    list_poems = get_poems()
    poems = []
    for poem in list_poems:
        poems.append(Poem(poem[1], poem[2], poem[3]))
    return render_template("index.html", poems=poems)

def get_poems():
    db = get_db()
    cursor = db.cursor()
    data = cursor.execute('SELECT * FROM poems;').fetchall()
    return data

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('poems.db')
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

if __name__ == '__main__':
    app.run(Debug=True)