import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")
    SECRET_KEY = os.getenv("SECRET_KEY", "your_secret_key")
    PROJECT_NAME = "fastapi-project"
    PROJECT_VERSION = "1"
    

settings = Settings()
