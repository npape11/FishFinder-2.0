import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Database Configuration
SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")  # Loaded from .env
SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disables unnecessary tracking

# Security
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")  # Secret key for authentication

