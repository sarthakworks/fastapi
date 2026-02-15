from fastapi import APIRouter
from pydantic import BaseModel

# Create APIRouter for POST endpoints
router = APIRouter()

# Define a data model (schema) for validating incoming JSON data
class Person(BaseModel):
    fname: str 
    lname: str 
    age: int

# Create a POST API endpoint at "/person" see readme 
@router.post("/person")
def add_person(p: Person):
    # 'p' automatically receives and validates the JSON body using the Person model
    # Construct a personalized message using the received data
    msg = "Hi! " + p.fname + " " + p.lname + ". Your age is " + str(p.age)
    # Return the message as a JSON response
    return {"message": msg}
