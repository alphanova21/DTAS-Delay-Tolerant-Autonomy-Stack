import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib

MODEL_FILE = "data/rover_model.pkl"

def train_model():
    df = pd.read_csv("data/training_data.csv")
    X = df.drop("action", axis=1)
    y = df["action"]

    model = DecisionTreeClassifier()
    model.fit(X, y)
    joblib.dump(model, MODEL_FILE)

def predict_action(input_data):
    model = joblib.load(MODEL_FILE)
    df = pd.DataFrame([input_data])
    return model.predict(df)[0]