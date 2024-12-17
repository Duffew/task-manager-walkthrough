from flask import render_template
from taskmanager import app, db # variables we just defined within __init__.py
from taskmanager.models import Category, Task

# create a basic app route to get the app running...
@app.route("/")
def home():
    return render_template("tasks.html")