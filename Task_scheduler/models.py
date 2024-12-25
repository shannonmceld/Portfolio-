from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import UserMixin
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey

db = SQLAlchemy()
bcrypt = Bcrypt()


class Users(db.Model, UserMixin):
    __tablename__ = 'users'  # Explicitly set the table name for consistency
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    hash_password = db.Column(db.String(128), nullable=False)  # Removed unique constraint

    def set_password(self, password):
        self.hash_password = bcrypt.generate_password_hash(password).decode('utf-8')
        
    def check_password(self, password):
        return bcrypt.check_password_hash(self.hash_password, password)


class Tasks(db.Model):
    __bind_key__ = 'tasks' 
    __tablename__ = 'tasks'  # Explicitly set the table name for consistency
       
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)  # Fixed ForeignKey to lowercase
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)  # Optional
    email = db.Column(db.String(120), nullable=False)
    due_date = db.Column(db.DateTime, nullable=False)
    reminder_time = db.Column(db.DateTime, nullable=False)
    completed = db.Column(db.Boolean, default=False)