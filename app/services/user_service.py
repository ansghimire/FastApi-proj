from sqlalchemy.orm import Session
from app.db.models.user import User
from app.schemas.user_schema import UserCreate
from app.core.security import hash_password

def create_user(db: Session, user_data: UserCreate) -> User:
    """Create a new user and store it in the database."""
    
    # Hash the password before storing
    hashed_password = hash_password(user_data.password)
    
    # Create user instance
    new_user = User(
        email=user_data.email,
        hashed_password=hashed_password
    )
    
    # Add user to DB session and commit
    db.add(new_user)
    db.commit()
    db.refresh(new_user)  # Refresh to get the latest DB state
    
    return new_user  # Return the created user object
