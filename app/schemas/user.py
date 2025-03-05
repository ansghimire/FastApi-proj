from pydantic import BaseModel, EmailStr

# Shared properties
class UserBase(BaseModel):
    email: EmailStr

# Schema for user creation (API request)
class UserCreate(UserBase):
    password: str

# Schema for user response (API response)
class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True  # Ensures SQLAlchemy compatibility

# Schema for login request
class UserLogin(BaseModel):
    email: EmailStr
    password: str

# Schema for token response
class Token(BaseModel):
    access_token: str
    token_type: str
