"""Example alternate startup file for Gunicorn.

In this sample the Flask app object is contained within the ``hello_app``
package (it provides an ``__init__.py`` and uses relative imports). Running
``webapp.py`` directly can trigger "Attempted relative import in non-package".

This module provides a small shim that imports the application object so you
can point Gunicorn at ``startup:app``.
"""

from hello_app.webapp import app  # noqa: F401
