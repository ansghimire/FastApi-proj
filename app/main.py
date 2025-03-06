from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.middlewares.logging_middleware import LoggingMiddleware
from app.db.session import engine
from app.db.base import Base
from app.common.error_handlers import custom_exception_handler, global_exception_handler
from app.common.exceptions import CustomHTTPException
from app.router import api_router  # Import the aggregated router

# Initialize the FastAPI app
app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)

# Middleware for logging
app.add_middleware(LoggingMiddleware)

# CORS (Modify as needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to specific domains in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register exception handlers
app.add_exception_handler(CustomHTTPException, custom_exception_handler)
app.add_exception_handler(Exception, global_exception_handler)

# Include the aggregated router from router.py
app.include_router(api_router)

# Database Initialization
def create_tables():
    """Create database tables if they don’t exist."""
    Base.metadata.create_all(bind=engine)

# Startup Event
@app.on_event("startup")
async def startup_event():
    create_tables()
    print("🚀 Application has started!")

# Shutdown Event
@app.on_event("shutdown")
async def shutdown_event():
    print("🛑 Application is shutting down!")

# Root Route
@app.get("/", tags=["Root"])
async def root():
    return {"message": "Welcome to the FastAPI Project!"}
