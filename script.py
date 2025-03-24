# Setting up the environment 
''' 
Fast api : for running the apis 
Uvicorn : fast Agi server that runs python web server 
joblib : for loading the model 

'''
import joblib
from fastapi import FastAPI , BackgroundTasks
from contextlib import asynccontextmanager
from pydantic import BaseModel
import asyncio
from typing import List


# loading the pretrained penguin classifier 
# predicts penguin species based on four features : length , depth , and the body mass 


# Loading the pretrained model 
'''
import os
file_path = "/Users/dikshanta/Documents/Fastapi_learning/penguin_classifier.pkl"

if os.path.exists(file_path):
    print("File exists.")
else:
    print("File not found. Check the path.")
model = joblib.load("/Users/dikshanta/Documents/Fastapi_learning/penguin_classifier.pkl")
print(f"Model Type: {type(model)}")

#fastapi prediction endpoint 
@app.post("/predict")
def predict(culmen_length_mm , culmen_depth_mm , 
            flipper_lenghth_mm , body_mass_g):
    
    features = [[culmen_length_mm , culmen_depth_mm , 
            flipper_lenghth_mm , body_mass_g]]
    

    prediction = model.predict(features)[0]
    return{"predicted speceies " : prediction}

'''


# Create the prediction endpoint
'''{
  "culmen_length_mm": 40.1,
  "culmen_depth_mm": 18.0,
  "flipper_length_mm": 200.0,
  "body_mass_g": 3500.0
}
'''


penguin_model = None

def load_model():
    global penguin_model
    model_path = "/Users/dikshanta/Documents/Fastapi_learning/penguin_classifier.pkl"
    penguin_model = joblib.load(model_path)
    print("Model loaded successfully")

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the model during app startup
    load_model()
    yield

app = FastAPI(lifespan= lifespan)

# predicting the model 
@app.post("/predict")
async def predict(culmen_length_mm: float, culmen_depth_mm: float,
                  flipper_length_mm: float, body_mass_g: float):
    features = [[culmen_length_mm, culmen_depth_mm, flipper_length_mm, body_mass_g]]
    prediction = penguin_model.predict(features)[0]
    return {"predicted species": prediction}


@app.get("/health")
async def health_check():
    if penguin_model is None:
        return {"status": "error", "message": "Model not loaded"}
    return {"status": "OK", "message": "Model loaded successfully"}


#Asynchronous processing

class Comment(BaseModel):
    text: str

# @app.post("/analyze")
# def analyze_sync(comment : Comment):
#     result = sentiment_model(comment.text)
#     return{"sentiment" : result}

async def sentiment_model(text: str):
    # Simulating async processing (replace with actual async function if available)
    import asyncio
    await asyncio.sleep(1)  # Simulate a delay
    return "Positive"  # Example output

# @app.post("/analyze")
# async def analyze_async(comment: Comment):
#     result = await sentiment_model(comment.text)
#     return {"sentiment": result}



@app.post("/analyze")
async def analyze_async(comment: Comment):
    result = await asyncio.to_thread(sentiment_model , comment.text)
    return {"sentiment": result}



# Background Tasks 
# - > manages the commenet processing queue 
# @app.post("/analyze_batch")
# async def analyze_batch(
#     comment :Comment,
#     background_tasks : BackgroundTasks
# ):
    
