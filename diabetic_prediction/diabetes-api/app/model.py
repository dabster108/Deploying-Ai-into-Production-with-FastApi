import joblib
import numpy as np
from app.schema import DiabetesInput

try:
    model = joblib.load("app/model.pkl")
except FileNotFoundError:
    raise FileNotFoundError("The model file 'app/model.pkl' was not found. Please ensure the file exists.")
except Exception as e:
    raise RuntimeError(f"An error occurred while loading the model: {e}")

def predict_diabetes(data: DiabetesInput) -> str:
    try:
        input_data = np.array([[
            data.Pregnancies,
            data.Glucose,
            data.BloodPressure,
            data.SkinThickness,
            data.Insulin,
            data.BMI,
            data.DiabetesPedigreeFunction,
            data.Age
        ]])
        prediction = model.predict(input_data)[0]
        return "Diabetic" if prediction == 1 else "Not Diabetic"
    except AttributeError as e:
        raise ValueError(f"Invalid input data: {e}")
    except Exception as e:
        raise RuntimeError(f"An error occurred during prediction: {e}")