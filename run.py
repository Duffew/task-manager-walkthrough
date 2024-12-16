# import os so that we can use environment variables within this file
import os
from taskmanager import app, db


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port = int(os.environ.get("PORT")), # port is an integer
        debug=os.environ.get("DEBUG")
    )