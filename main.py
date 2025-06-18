"""
Main entry point for running the FastAPI application.
Loads environment variables, sets up the app import path, and starts the server if run directly.
"""
import sys
from pathlib import Path
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Add app directory to sys.path
sys.path.append(str(Path(__file__).parent / "app"))

from app.main import app

if __name__ == "__main__":
    import uvicorn
    app_host = os.getenv("APP_HOST", "0.0.0.0")
    app_port = int(os.getenv("APP_PORT", 8000))
    uvicorn.run("app.main:app", host=app_host, port=app_port, reload=True)