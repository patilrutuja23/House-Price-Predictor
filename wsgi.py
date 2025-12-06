"""
WSGI entry point for Vercel serverless deployment.
This file is required by Vercel's Python runtime.
"""

import sys
import os

# Add server directory to path so imports work
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'server'))

# Import the Flask app from server.py
from server import app

# Vercel looks for this variable
__all__ = ['app']
