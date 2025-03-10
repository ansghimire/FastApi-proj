from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.endpoints import auth, users, posts
from app.core.config import settings
from app.middlewares.logging_middleware import LoggingMiddleware
from app.db.session import engine, Base
from app.dependencies import get_db

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

# Include routers
app.include_router(auth.router, prefix="/api/v1/auth", tags=["Auth"])
app.include_router(users.router, prefix="/api/v1/users", tags=["Users"])
app.include_router(posts.router, prefix="/api/v1/posts", tags=["Posts"])

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

