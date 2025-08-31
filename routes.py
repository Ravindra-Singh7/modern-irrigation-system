from flask import Blueprint, render_template, request
from irrigation_model import predict_irrigation
from models.sensor_data import db, SensorData

irrigation_bp = Blueprint("irrigation", __name__)

@irrigation_bp.route("/")
def home():
    return render_template("index.html")

@irrigation_bp.route("/predict", methods=["POST"])
def predict():
    temp = float(request.form["temperature"])
    humidity = float(request.form["humidity"])
    soil = float(request.form["soil_moisture"])

    # Save to DB
    data = SensorData(temperature=temp, humidity=humidity, soil_moisture=soil)
    db.session.add(data)
    db.session.commit()

    # Get prediction
    result = predict_irrigation(temp, humidity, soil)

    return render_template("result.html", result=result)

