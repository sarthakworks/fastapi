from fastapi import FastAPI
import uvicorn

# Create FastAPI object
app = FastAPI()

# Add a GET method to the "/" endpoint
@app.get("/")
def root():
    return {"message": "Hello from FastAPI!"}


# Define a GET API endpoint "/greet" with Query parameters
# In Browser, access the endpoint like this:
# "/greet?first_name=sarthak&last_name=bansal"
@app.get("/greet")
def greet(first_name: str, last_name: str):
    return {"message": f"Hello {first_name} {last_name}!"}


# Define a GET API endpoint "/hello" with Path parameters
# In Browser, access the endpoint like this: "/hello/Amar/Kumar"
@app.get("/hello/{fname}/{lname}")
def get_item(fname: str, lname: str):
    msg = "Hello! " + fname + " " + lname
    return {"message": msg}

# Import BaseModel from Pydantic to define structured request body models
from pydantic import BaseModel

# Define a data model (schema) for validating incoming JSON data
class Person(BaseModel):
    fname: str 
    lname: str 
    age: int

# Create a POST API endpoint at "/person" see readme 
@app.post("/person")
def add_person(p: Person):
    # 'p' automatically receives and validates the JSON body using the Person model
    # Construct a personalized message using the received data
    msg = "Hi! " + p.fname + " " + p.lname + ". Your age is " + str(p.age)
    # Return the message as a JSON response
    return {"message": msg}


# Start application
if __name__ == "__main__":
    uvicorn.run(app)