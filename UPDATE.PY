from flask import Blueprint, request, jsonify
from rover_controller import execute_batch
from ai_module import anomaly_detection
from ml_module import train_model, predict_action
from safety_module import apply_safety
from database import db
from models import CommandLog, AnomalyLog, PredictionLog, TrainingLog
import json

rover_bp = Blueprint("rover", _name_)

@rover_bp.route("/execute", methods=["POST"])
def execute():
    commands = request.json.get("commands", [])
    result = execute_batch(commands)

    log = CommandLog(commands=json.dumps(commands), result=json.dumps(result))
    db.session.add(log)
    db.session.commit()

    return jsonify({"status": "success", "result": result})

@rover_bp.route("/anomaly", methods=["POST"])
def anomaly():
    data = request.json
    action = anomaly_detection(data)
    safe_action = apply_safety(action)

    log = AnomalyLog(input_data=json.dumps(data), decision=safe_action)
    db.session.add(log)
    db.session.commit()

    return jsonify({"decision": safe_action})

@rover_bp.route("/learn", methods=["POST"])
def learn():
    train_model()
    log = TrainingLog(status="trained")
    db.session.add(log)
    db.session.commit()
    return jsonify({"status": "model trained"})

@rover_bp.route("/predict", methods=["POST"])
def predict():
    data = request.json
    prediction = predict_action(data)

    log = PredictionLog(input_data=json.dumps(data), prediction=prediction)
    db.session.add(log)
    db.session.commit()

    return jsonify({"prediction": prediction})

# Extra endpoint to view logs
@rover_bp.route("/logs", methods=["GET"])
def logs():
    commands = CommandLog.query.order_by(CommandLog.created_at.desc()).limit(5).all()
    anomalies = AnomalyLog.query.order_by(AnomalyLog.created_at.desc()).limit(5).all()
    preds = PredictionLog.query.order_by(PredictionLog.created_at.desc()).limit(5).all()
    train = TrainingLog.query.order_by(TrainingLog.created_at.desc()).limit(5).all()

    return jsonify({
        "commands": [{"id":c.id,"commands":c.commands,"result":c.result,"time":c.created_at.isoformat()} for c in commands],
        "anomalies": [{"id":a.id,"input":a.input_data,"decision":a.decision,"time":a.created_at.isoformat()} for a in anomalies],
        "predictions": [{"id":p.id,"input":p.input_data,"prediction":p.prediction,"time":p.created_at.isoformat()} for p in preds],
        "training": [{"id":t.id,"status":t.status,"time":t.created_at.isoformat()} for t in train]
    })