from fastapi import FastAPI, HTTPException
from pydantic import BaseModel  # defines the data structure 

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
