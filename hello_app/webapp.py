"""Entry point for the application.

This module intentionally imports the application object so the `flask`
command can discover the app. It should not contain secrets in source.
"""

import os
import logging

# For application discovery by the 'flask' command.
from . import app  # noqa: F401

# Import for side-effects: this module registers routes with the app.
from . import views  # noqa: F401

# Time-saver: print a URL you can Ctrl+click to open in a browser.
# print('http://127.0.0.1:5000/hello/VSCode')

# Read AWS secret from environment to avoid hardcoding credentials.
AWS_SECRET_KEY = os.environ.get("AWS_SECRET_KEY")
if not AWS_SECRET_KEY:
	logging.warning(
		"AWS_SECRET_KEY not set in environment; some features may fail."
	)
	
    # Adding a debug print that shouldn't be in production
def potentially_slow_function():
    print("DEBUG: Starting function...") 
    import time
    time.sleep(1) # Hardcoded delay
    return True