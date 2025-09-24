from datetime import datetime
from database import db

class CommandLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    commands = db.Column(db.Text, nullable=False)
    result = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class AnomalyLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    input_data = db.Column(db.Text, nullable=False)
    decision = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class PredictionLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    input_data = db.Column(db.Text, nullable=False)
    prediction = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class TrainingLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)