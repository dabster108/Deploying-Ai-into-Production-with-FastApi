from fastapi import FastAPI


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
def get_student(student_id: int):   # giving the student id with the datatype
    return students[student_id]