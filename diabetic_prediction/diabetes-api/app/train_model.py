import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

# Create directory if it doesn't exist
os.makedirs("app", exist_ok=True)

# Sample dataset for diabetes prediction
# You should replace this with your actual dataset if available
try:
    # Try to load the Pima Indians Diabetes dataset
    df = pd.read_csv('https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv', 
                     header=None,
                     names=['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 
                            'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age', 'Outcome'])
except:
    # If dataset can't be loaded, create synthetic data
    print("Creating synthetic data for demonstration purposes")
    from sklearn.datasets import make_classification
    X, y = make_classification(n_samples=768, n_features=8, n_classes=2, random_state=42)
    df = pd.DataFrame(X, columns=['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 
                                 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age'])
    df['Outcome'] = y

# Prepare data
X = df.drop('Outcome', axis=1).values
y = df['Outcome'].values

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a simple model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate the model
accuracy = model.score(X_test, y_test)
print(f"Model accuracy: {accuracy:.4f}")

# Save the model
model_path = "app/model.pkl"
joblib.dump(model, model_path)
print(f"Model saved to {model_path}")