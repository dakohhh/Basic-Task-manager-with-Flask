import sqlite3
import bcrypt

from flask import Flask, redirect, render_template, request, url_for, session
from db import create_database
from db import add_a_task
from db import update_task
from db import delete_task
from db import clear_all_task
from db import test_resturn
from db import generate_row_id
from db import get_all_task




app = Flask(__name__)
app.secret_key = "rapemanbruh"
app.debug = True
create_database()


@app.route("/", methods=["POST", "GET"])
def add_task():
    #wis = sqlite3.connect()
    if request.method == "POST":
        add_a_task(request.form.get('tname'))
        print(get_all_task())
        return redirect(url_for('add_task'))
    return render_template("add_task.html", all_task=get_all_task())



@app.route("/edit_task", methods=["POST", "GET"])
def edit_task():
    print(dict(request.values))
    return render_template("task.html")

@app.errorhandler(404)
def error_handler(e):
    return render_template("error404.html")



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")