from fastapi import FastAPI
import uvicorn
import asyncio
from app.routers import items, containers
from app.init_db import init_db
from app.tasks import update_containers_randomly

# Create FastAPI app
app = FastAPI(
    title="Sample FastAPI Project",
    description="A sample FastAPI project with CRUD operations for items and containers",
    version="1.0.0"
)

# Include routers
app.include_router(items.router)
app.include_router(containers.router)

# Initialize database tables and start background tasks on startup
@app.on_event("startup")
async def startup_event():
    init_db()
    # Start the background task
    asyncio.create_task(update_containers_randomly())

# Root route
@app.get("/")
async def root():
    """Root endpoint returning a welcome message."""
    return {
        "message": "Welcome to Sample FastAPI Project",
        "docs": "/docs",
        "endpoints": {
            "items": "/items",
            "containers": "/containers"
        }
    }

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True) 