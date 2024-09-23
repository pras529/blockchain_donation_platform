from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from web3 import Web3
import os

app = Flask(__name__)

# Load configuration from config.py or environment variables
app.config.from_pyfile('config.py')

# Initialize the database
db = SQLAlchemy(app)

# Initialize Web3 for blockchain integration
blockchain_url = os.getenv('BLOCKCHAIN_URL', 'http://127.0.0.1:8545')
w3 = Web3(Web3.HTTPProvider(blockchain_url))

# Import routes
from app import routes

if __name__ == '__main__':
    app.run(debug=True)
