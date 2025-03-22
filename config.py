from pathlib import Path
import os
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

basedir = Path(__file__).parent.resolve()
connexion_app = connexion.FlaskApp(__name__, specification_dir=basedir)
app = connexion_app.app


# get db uri from Render
database_url = os.environ.get("DATABASE_URL", f"sqlite:///{basedir / 'thanos3.db'}")

# Fix potential Postgres URL format issue (Render uses postgres:// but SQLAlchemy needs postgresql://)
if database_url and database_url.startswith("postgres://"):
    database_url = database_url.replace("postgres://", "postgresql://", 1)


# Configure the database
app.config["SQLALCHEMY_DATABASE_URI"] = database_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


app.config["DEBUG"] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)