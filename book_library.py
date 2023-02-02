#Book Library:
#A web application that allows users to search, borrow, and return books.

from flask import Flask, request, render_template, redirect, url_for
import sqlite3

app = Flask(__name__)

def connect_db():
    conn = sqlite3.connect("library.db")
    return conn

@app.route("/")
def home():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM books")
    books = cur.fetchall()
    return render_template("home.html", books=books)

@app.route("/borrow/<int:id>")
def borrow(id):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("UPDATE books SET available=0 WHERE id=?", (id,))
    conn.commit()
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
