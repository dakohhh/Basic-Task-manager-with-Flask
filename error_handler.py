from flask import Flask, redirect, render_template
from app import app





@app.errorhandler(404)
def error_handler(e):
    return render_template("error404.html")
