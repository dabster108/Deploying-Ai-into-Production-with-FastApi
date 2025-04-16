from fastapi import FastAPI
from app.schema import DiabetesInput
from app.model import predict_diabetes

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Diabetes Prediction API"}

@app.post("/predict")
def predict(data: DiabetesInput):
    result = predict_diabetes(data)
    return {"prediction": result}
