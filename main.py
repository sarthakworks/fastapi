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

# Start application
if __name__ == "__main__":
    uvicorn.run(app)