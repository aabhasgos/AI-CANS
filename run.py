"""
AI-CNAS Backend Runner
Run this from the project root: python run.py
"""
import sys
import os

# Add the project root to Python path so 'backend' package imports work
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import uvicorn

if __name__ == "__main__":
    uvicorn.run("backend.main:app", host="0.0.0.0", port=8000, reload=True)
