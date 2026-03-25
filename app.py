from flask import Flask, render_template, request, redirect
import sqlite3
import string
import random

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('urls.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS urls
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  original TEXT,
                  short TEXT UNIQUE)''')
    conn.commit()
    conn.close()

init_db()

def generate_short():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(6))

@app.route("/", methods=["GET", "POST"])
def home():
    short_url = ""
    if request.method == "POST":
        original_url = request.form["url"]

        short_code = generate_short()

        conn = sqlite3.connect('urls.db')
        c = conn.cursor()

        try:
            c.execute("INSERT INTO urls (original, short) VALUES (?, ?)", 
                      (original_url, short_code))
            conn.commit()
        except:
            pass

        conn.close()

        short_url = request.host_url + short_code

    return render_template("index.html", short_url=short_url)

@app.route("/<short_code>")
def redirect_url(short_code):
    conn = sqlite3.connect('urls.db')
    c = conn.cursor()
    c.execute("SELECT original FROM urls WHERE short=?", (short_code,))
    result = c.fetchone()
    conn.close()

    if result:
        return redirect(result[0])
    else:
        return "<h2 style='text-align:center'>❌ URL not found</h2>"

if __name__ == "__main__":
    app.run(debug=True)