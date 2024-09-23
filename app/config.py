import os

# Flask config
SECRET_KEY = os.getenv('SECRET_KEY', 'mysecretkey')
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///db.sqlite3')
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Vultr API configuration
VULTR_API_KEY = os.getenv('VULTR_API_KEY')
