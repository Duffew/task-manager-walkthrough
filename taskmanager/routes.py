from flask import render_template, request, redirect, url_for
from taskmanager import app, db # variables we just defined within __init__.py
from taskmanager.models import Category, Task

# create a basic app route to get the app running...
@app.route("/")
def home():
    return render_template("tasks.html")


# create an app route for categories.html
@app.route("/categories")
def categories():
    # updated route after category cards added to categories.html
    categories = list(Category.query.order_by(Category.category_name).all())
    return render_template("categories.html", categories=categories)


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = Category(category_name=request.form.get("category_name"))
        db.session.add(category)
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("add_category.html")


@app.route("/edit_category/<int:category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    return render_template("edit_category.html")