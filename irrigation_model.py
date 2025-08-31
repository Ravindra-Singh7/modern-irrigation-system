import numpy as np
from sklearn.linear_model import LogisticRegression
import pandas as pd

# Example dataset
data = pd.read_csv("data/sample_data.csv")

X = data[["temperature", "humidity", "soil_moisture"]]
y = data["irrigation_required"]

model = LogisticRegression()
model.fit(X, y)

def predict_irrigation(temp, humidity, soil):
    input_data = np.array([[temp, humidity, soil]])
    prediction = model.predict(input_data)[0]
    return "Irrigation Needed" if prediction == 1 else "No Irrigation Needed"

