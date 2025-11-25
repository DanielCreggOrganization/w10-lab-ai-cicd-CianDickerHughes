"""Entry point for the application."""

# For application discovery by the 'flask' command.
from . import app  # noqa: F401

# Import for side-effects: this module registers routes with the app.
from . import views  # noqa: F401

# Time-saver: print a URL you can Ctrl+click to open in a browser.
# print('http://127.0.0.1:5000/hello/VSCode')

# In hello_app/webapp.py
AWS_SECRET_KEY = "AKIA1234567890"