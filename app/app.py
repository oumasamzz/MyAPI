from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

# Create Flask application instance
app = Flask(__name__)

# Configuration for SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable modification tracking

# Initialize SQLAlchemy database
db = SQLAlchemy(app)

