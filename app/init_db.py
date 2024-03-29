from app import app, db

# Initialize SQLite database
with app.app_context():
    db.create_all()