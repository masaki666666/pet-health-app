from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    species = db.Column(db.String(64), nullable=False)
    birthdate = db.Column(db.Date, nullable=False)
    weight = db.Column(db.Float, nullable=False)

class HealthLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pet_id = db.Column(db.Integer, db.ForeignKey('pet.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    weight = db.Column(db.Float, nullable=False)
    activity_level = db.Column(db.String(20), nullable=False)
    appetite = db.Column(db.String(20), nullable=False)
    coat_condition = db.Column(db.String(20), nullable=False)
    bowel_movement = db.Column(db.String(20), nullable=False)
    urine_output = db.Column(db.String(20), nullable=False)

class EventLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pet_id = db.Column(db.Integer, db.ForeignKey('pet.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    event_type = db.Column(db.String(20), nullable=False)
    notes = db.Column(db.String(200), nullable=True)

class PetImage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pet_id = db.Column(db.Integer, db.ForeignKey('pet.id'), nullable=False)
    filename = db.Column(db.String(100), nullable=False)
