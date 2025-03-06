from fastapi import APIRouter
from app.api.v1.endpoints import auth, users, posts

api_router = APIRouter()

# Register the individual endpoint routers with appropriate prefixes and tags
api_router.include_router(auth.router, prefix="/api/v1/auth", tags=["Auth"])
# api_router.include_router(users.router, prefix="/api/v1/users", tags=["Users"])
# api_router.include_router(posts.router, prefix="/api/v1/posts", tags=["Posts"])
