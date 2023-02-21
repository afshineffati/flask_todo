from flask import Flask, render_template, abort
from model import db

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/todo/<int:index>")
def todos(index):
    try:
        todo = db[index]
        return render_template("todo.html", todo=todo, index=index)
    except IndexError:
        abort(404) 