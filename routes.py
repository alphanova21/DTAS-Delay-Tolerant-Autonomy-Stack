from flask import Blueprint, request, jsonify
from rover_controller import execute_batch
from ai_module import anomaly_detection
from ml_module import train_model, predict_action
from safety_module import apply_safety

rover_bp = Blueprint("rover", _name_)

@rover_bp.route("/execute", methods=["POST"])
def execute():
    commands = request.json.get("commands", [])
    result = execute_batch(commands)
    return jsonify({"status": "success", "result": result})

@rover_bp.route("/anomaly", methods=["POST"])
def anomaly():
    data = request.json
    action = anomaly_detection(data)
    safe_action = apply_safety(action)
    return jsonify({"decision": safe_action})

@rover_bp.route("/learn", methods=["POST"])
def learn():
    train_model()
    return jsonify({"status": "model trained"})

@rover_bp.route("/predict", methods=["POST"])
def predict():
    data = request.json
    prediction = predict_action(data)
    return jsonify({"prediction": prediction}