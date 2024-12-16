import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# import the env.py file so that we can use the hidden environment variables
if os.path.exists("env.py"):
    import env

# create an instance of the imported Flask() class
app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")

# create an instance of the imported SQLAlchemy() class
db = SQLAlchemy(app)

# we define this import here as it relies on the 'app' and 'db' 
# varaibles above - those variables must be defined first
from taskmanager import routes
