from fastapi import FastAPI, HTTPException
from pydantic import BaseModel , Field # defines the data structure 
from pydantic import ValidationError , validator, model_validator 
import numpy as np 
from scorer import CommentMetrics, CommentScorer
from typing import List

from fastapi.responses import PlainTextResponse
app = FastAPI()

@app.get("/item/{item_id}")  # Fixed the path variable naming
async def read_item(item_id: int):  # Match function parameter with the path variable
    if item_id == 42:
        raise HTTPException(status_code= 404 , detail=  "Item not found ")
    return {"item_id": item_id}  # Use correct variable name in response

db = {} # empty dictionary 
class Item(BaseModel):
    name : str
    price : float
@app.post("/items", status_code= 201) # post method to send information
def create_item(item : Item):
    db[item.name] = item.dict()
    return{"message " : f"Created {item.name}"}

# 200 : default for sucess 
# 404 not found  : resource not found 
# 201 : sucessfully object created 

class User(BaseModel): # so the items now will inherit from the basemodel 
    name : str 
    email : str 
    age : int 




# Validation error 
try : 
    invalid_user = User(username = "dikshata" , email = "dikshanta@gmail.com",
                        age= 30)
    print("Invalid user : "  ,  invalid_user)
except ValidationError as e :
    print("Validation error ", e )



users_db = {}

@app.post("/users", response_model=User)
async def create_user(user: User):
    users_db[user.name] = user  # Store the user in a dictionary
    return user

@app.get("/users/{user_name}", response_model=User)
def get_user(user_name: str):
    if user_name not in users_db:
        return {"error": "User not found"}
    return users_db[user_name]


class CommentMetrics(BaseModel):
    length : int 
    user_karma : int 
    report_count : int 

class CommentText(BaseModel):
    content : str 


class CommentMetrics(BaseModel):
    length: float
    user_karma: float
    report_count: float

class CommentScorer:
    def __init__(self):
        # You can load a trained model here if needed
        pass


# Assuming you have a model instance
model = CommentScorer()  # Ensure CommentScoer is properly defined

@app.post("/predict/comment")
def predict_score(data: CommentMetrics):
    # Convert the data into a 2D numpy array
    features = np.array([[data.length, data.user_karma, data.report_count]])

    # Predict using the model
    prediction = model.predict(features)

    return {
        'prediction': round(prediction[0], 2),
        'input': data.dict()
    }


# Endpoint for textual input 

@app.post("/analyze-text")
def analyze(comment: CommentText):
    forbidden = ["spam", "fake", "hate", "free", "signup"]
    text_lower = comment.content.lower()  # Convert text to lowercase

    for word in forbidden:
        if word in text_lower:
            return {"issue": word}  # Return immediately when a forbidden word is found

    return {"issue": "No issues detected"}



@app.post("/predict_trust")
def predict_trust(comment: CommentMetrics):
    # Convert input and extract comment metrics
    features = np.array([[
        comment.length,
        comment.user_reputation,
        comment.report_count
    ]])
    # Get prediction from model 
    score = model.predict(features)
    return {
        "trust_score": round(score, 2),
        "comment_metrics": comment.dict()
    }


#Pydantic validators  
class User(BaseModel):
    username : str  = Field (... , min_length = 3 , max_length = 10)
    age : int
    email : str
    @validator('age')
    def age_credentials(cls,age):
        if age < 18:
            raise ValueError("Must be atleast 18")
        return age
    
    @validator('email')
    def email_must_be_example_domain(cls, user_email):
        if not user_email.endswith("@gmail.com"):
            raise ValueError('Email must be from the @gmail.com domain')
        return user_email
    

@app.post("/register")
# Validate incoming user data with a pydantic model
def register_user(user: User):
    return {"status": "success", "user": user.dict()}
  

# defining request structure 
sentiment_model = None  

class PredictionRequest(BaseModel):
    text: str 

class PredictionResponse(BaseModel):
    text: str 
    sentiment: str 
    confidence: float 

@app.post("/predict/sentiment", response_model=PredictionResponse)
def predict_sentiment(request: PredictionRequest):
    global sentiment_model
    
    if sentiment_model is None:
        raise HTTPException(
            status_code=503,
            detail="Model not loaded"
        )

    try:
        result = sentiment_model(request.text)  # Fixed incorrect attribute name
        return PredictionResponse(
            text=request.text,
            sentiment=result[0]["label"],
            confidence=result[0]["score"]  # Fixed key mismatch
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Prediction failed: {str(e)}"
        )
    

class Foo(BaseModel):
    count : int 

class Bar(BaseModel):
    foo : Foo

class OrderItem(BaseModel):
    name : str 
    quantity : int 

class ResturantOrder(BaseModel):
    customer_name  : str 
    items : List[OrderItem]


    # custome model validators 
    from fastapi.exceptions import(
        RequestValidationError
    )

    from pydantic import(
        BaseModel,
        model_validator
    )
    
class Order(BaseModel):
    items: int

    @model_validator(mode="after")
    def validate_after(self):
        if self.items == 0:
            raise ValueError("No items in order")
        return self

@app.post("/order")
async def create_order(order: Order):
    return {"message": "Order created successfully", "items": order.items}



#@app.exception_handler(RequestValidationError)