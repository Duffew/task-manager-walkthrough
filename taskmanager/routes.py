from flask import render_template
from taskmanager import app, db # variables we just defined within __init__.py

# create a basic app route to get the app running...
@app.route("/")
def home():
    return render_template("base.html")