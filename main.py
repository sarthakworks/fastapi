from fastapi import FastAPI
import uvicorn

# Import routers from separate files
from routes_get import router as get_router
from routes_post import router as post_router

# Create FastAPI object
app = FastAPI()

# Include routers
app.include_router(get_router)
app.include_router(post_router)

# Start application
if __name__ == "__main__":
    uvicorn.run(app)