from fastapi import FastAPI
import uvicorn

# Create FastAPI object
app = FastAPI()

# Add a GET method to the "/" endpoint
@app.get("/")
def root():
    return {"message": "Hello from FastAPI!"}

# Start application
if __name__ == "__main__":
    uvicorn.run(app)