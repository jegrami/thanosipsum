from pathlib import Path
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

basedir = Path(__file__).parent.resolve()
connexion_app = connexion.FlaskApp(__name__, specification_dir=basedir)
app = connexion_app.app

app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{basedir / 'thanos3.db'}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["DEBUG"] = True

db = SQLAlchemy(app)
ma = Marshmallow(app)