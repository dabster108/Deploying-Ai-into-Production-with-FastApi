import joblib
import numpy as np
from app.schema import DiabetesInput
import os
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Path to the model file
MODEL_PATH = "app/model.pkl"

# Function to train and save a model if it doesn't exist
def create_model():
    try:
        from sklearn.ensemble import RandomForestClassifier
        from sklearn.datasets import make_classification
        from sklearn.model_selection import train_test_split
        
        logger.info("Training a new model...")
        
        # Create synthetic data for demonstration
        X, y = make_classification(n_samples=768, n_features=8, n_classes=2, random_state=42)
        
        # Split dataset
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Train a simple model
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)
        
        # Save the model
        os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)
        joblib.dump(model, MODEL_PATH)
        logger.info(f"Model saved to {MODEL_PATH}")
        
        return model
    except Exception as e:
        logger.error(f"Failed to create model: {e}")
        raise RuntimeError(f"Failed to create model: {e}")

# Try to load the model or create it if it doesn't exist
try:
    model = joblib.load(MODEL_PATH)
    logger.info("Model loaded successfully")
except FileNotFoundError:
    logger.warning(f"Model file '{MODEL_PATH}' not found. Creating a new model...")
    model = create_model()
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