# Setting up the environment 
''' 
Fast api : for running the apis 
Uvicorn : fast Agi server that runs python web server 
joblib : for loading the model 

'''
import joblib
from fastapi import FastAPI
app = FastAPI()

# loading the pretrained penguin classifier 
# predicts penguin species based on four features : length , depth , and the body mass 


# Loading the pretrained model 
model = joblib.load('/Users/dikshanta/Documents/Fastapi_learning/penguin_classifier.pkl')
print(type(model))

#fastapi prediction endpoint 
@app.post("/predict")
def predict(culmen_length_mm , culmen_depth_mm , 
            flipper_lenghth_mm , body_mass_g):
    
    features = [[culmen_length_mm , culmen_depth_mm , 
            flipper_lenghth_mm , body_mass_g]]
    

    prediction = model.predict(features)[0]
    return{"predicted speceies " : prediction}