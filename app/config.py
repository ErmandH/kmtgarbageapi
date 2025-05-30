import os
from urllib.parse import quote_plus
from dotenv import load_dotenv

# Load environment variables from .env file if it exists
load_dotenv()


# Construct the DATABASE_URL with escaped characters
DATABASE_URL = os.getenv("DB_URL", "fastapi")

# API Settings
API_PREFIX = "/api"
PROJECT_NAME = "Sample FastAPI Project"
DEBUG = os.getenv("DEBUG", "False").lower() == "true" 