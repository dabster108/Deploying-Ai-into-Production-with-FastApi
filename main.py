from fastapi import FastAPI, Path
from typing import Optional

app = FastAPI()
# fast api is an object and we are first creating the instance of the object 
# amazon.com/create-user and this create user is the path end point 
# There are diffrent types of endpoint methods 
'''
GET - Get an information/ data 
POST - Create a new information/data -- CREATING new object 
PUT - Update an information/data
DELETE - Delete an information/data
'''

students = {
    1: {"name": "John",
        "age": 20,
        "class" : "Year 18"
        }
}

@app.get("/")
def index():
    return {"Name" : "First Data"}


@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(..., description="input the Id of the student", gt = 0 , lt = 5)):
    return students[student_id]

# gt - greater than , lt - lesser than , ge - greater than equals to , le - less than or equals to 
# query parameter is used to pass a value into a url 
@app.get("/get-by-name")
def get_student(name:str):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data" : "Not found"}