"""
WSGI config for myproject project.
"""

import os
from django.core.wsgi import get_wsgi_application
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set the Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")

# Get the WSGI application
application = get_wsgi_application()