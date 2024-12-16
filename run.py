# import os so that we can use environment variables within this file
import os
from taskmanager import app


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=os.environ.get("DEBUG")
    )

app = create_app()
with app.app_context():
    db.create_all()