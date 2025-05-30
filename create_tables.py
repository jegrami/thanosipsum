from config import app, db
from models import Quote  # import all models that should be created

with app.app_context():
    db.create_all()
    print("✅ Tables created successfully.")
