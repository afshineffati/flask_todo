from flask import Flask, render_template, abort, jsonify, request, redirect, url_for
from model import db, save_db

app = Flask(__name__)


@app.route("/")
def home():
    return render_template(
        "home.html")


@app.route("/todos")
def todos():
    return render_template("todo_list.html",
                           todos=db)

@app.route("/todos/<int:index>")
def todo_view(index):
    try:
        todo = db[index]
        return render_template("todo_view.html", 
                            todo=todo, 
                            index=index,
                            max_index=len(db)-1)
    except IndexError:
        abort(404) 


@app.route('/add_todo', methods=["GET", "POST"])
def add_todo():
    if request.method == "POST":    #user has submitted data and we have to process it
        todo = {"Title":request.form['title'],
                "Notes":request.form['notes']}
        db.append(todo)
        save_db()
        return redirect(url_for('todo_view', index=len(db)-1))
    else:           #when user first visits this page, it would be GET
        return render_template("add_todo.html")


@app.route("/remove_todo/<int:index>", methods=["GET", "POST"])
def remove_todo(index):
    try:
        if request.method == "POST":
            db.pop(index)
            save_db()
            return redirect(url_for('todos'))
        else:
            return render_template("remove_todo.html", 
                                    todo=db[index])
    except IndexError:
        abort(404)





@app.route("/api/todos")
def api_todos():
    return jsonify(db)


@app.route("/api/todos/<int:index>")
def api_todo_view(index):
    try:
        return db[index]
    except IndexError:
        abort(404) 


