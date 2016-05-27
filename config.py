import os

PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))

DEBUG = False
SECRET_KEY = 'your-secret-key'
SITE_TITLE = 'Areacodely'
DEFAULT_ROLE = 'user'

from config_prod import *