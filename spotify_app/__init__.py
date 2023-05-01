
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, static_url_path="/static", static_folder='static')
app.config["SECRET_KEY"] = "9b24f821ee1c54c8236015ef4e8dc50b"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blog_site.db"
app._static_folder = "static"
db = SQLAlchemy(app)


app.app_context().push()

# Importing routes after the app is initialized to prevent a circular import.
from spotify_app import routes
