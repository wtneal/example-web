import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
CSRF_ENABLED = True

DEBUG = os.getenv('DEBUG', False)
SECRET_KEY = os.getenv('SECRET_KEY', None)
