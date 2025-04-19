import joblib
import numpy as np
import os
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Path to the model file - use a relative path from this file
MODEL_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "model.pkl")

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
        logger.info(f"Saving model to: {MODEL_PATH}")
        joblib.dump(model, MODEL_PATH)
        
        # Verify the file was created
        if os.path.exists(MODEL_PATH):
            logger.info(f"Model successfully saved to {MODEL_PATH}")
        else:
            logger.error(f"Model file was not created at {MODEL_PATH}")
            
        return model
    except ImportError as e:
        logger.error(f"Missing dependency: {e}")
        logger.error("Please install required packages: pip install scikit-learn joblib")
        raise RuntimeError(f"Missing dependency: {e}")
    except Exception as e:
        logger.error(f"Failed to create model: {e}")
        import traceback
        logger.error(traceback.format_exc())
        raise RuntimeError(f"Failed to create model: {e}")

# Definition that can be imported elsewhere
def get_model():
    """Load the model or create it if it doesn't exist."""
    try:
        if os.path.exists(MODEL_PATH):
            logger.info(f"Loading model from {MODEL_PATH}")
            return joblib.load(MODEL_PATH)
        else:
            logger.info(f"Model file not found. Creating new model...")
            return create_model()
    except Exception as e:
        logger.error(f"Error loading/creating model: {e}")
        raise

# Define a prediction function that doesn't rely on the schema
def predict(features):
    """Make a prediction using the loaded model.
    
    Args:
        features: List or array of features in the order:
            [Pregnancies, Glucose, BloodPressure, SkinThickness,
             Insulin, BMI, DiabetesPedigreeFunction, Age]
    
    Returns:
        str: "Diabetic" or "Not Diabetic"
    """
    model = get_model()
    input_data = np.array([features])
    prediction = model.predict(input_data)[0]
    return "Diabetic" if prediction == 1 else "Not Diabetic"

# If this file is run directly, create the model
if __name__ == "__main__":
    model = create_model()
    logger.info("Model creation complete")