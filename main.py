from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

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
        "year" : "Year 18"
        }
}


class Student(BaseModel):
    name :str
    age:int 
    year: str
    


class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[str] = None

@app.get("/")
def index():
    return {"Name" : "First Data"}


@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(..., description="input the Id of the student", gt = 0 , lt = 9)):
    return students[student_id]

# gt - greater than , lt - lesser than , ge - greater than equals to , le - less than or equals to 
# query parameter is used to pass a value into a url 
@app.get("/get-by-name/{student_id}")
def get_student(* , student_id : int ,name:str , test:int):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data" : "Not found"}



@app.post("/create-student/{student_id}")                ## to create a new information 
def create_student(student_id :int, student: Student):
    if student_id in students:
        return{"Error"  :"Student data already exits"}
    
    students[student_id] = student
    return students[student_id]

#put method 
@app.put("/update-student/{student_id}")
def update_student(student_id : int, student:Student):
    if student_id not in students:
        return {"Error" : "Student_id does exits"} 
    
    
    if student.name !=None:
        students[student_id].name = student.name
    
    if student.age !=None:
        students[student_id].age = student.age
        
    if student.year !=None:
        students[student_id].year = student.year
        
        

    return students[student_id]
    


@app.delete("/delete-student/{student_id}")
def delete_student(student_id:int, student = Student):
    if student_id not in students:
        return {"Error" : "Student doesnot exits"}
    
    
    del students[student_id]
    return {"Message" : "Student Deleted Succesfully"}