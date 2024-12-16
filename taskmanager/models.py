# in the prevsious lessons we imported each column type by name
# using the db variable automatically brings the column types with it so
# db.Column can be used when defining the class variables
from taskmanager import db

# create 2 tables represeneted by class-based models using SQLAlchemy's ORM

class Category(db.Model):
    # schema for the Category model
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(25), unique=True, nullable=False) # max character count of 25
    # add this variable to manage the ondelete="CASCADE" feature of the Task class
    tasks = db.relationship("Task", backref="category", cascade="all, delete", lazy=True)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.category_name


class Task(db.Model):
    # schema for the Task model
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(50), unique=True, nullable=False) # nullable=False means 'required'
    task_description = db.Column(db.Text, nullable=False) # 'Text' allows for longer strings
    is_urgent = db.Column(db.Boolean, default=False, nullable=False)
    due_date = db.Column(db.Date, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id", ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return "#0 - Task: {1} | Urgent: {2}".format(
            self.id, self.task.name, self.is_urgent
        )