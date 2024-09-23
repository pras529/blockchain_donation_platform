from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_session import Session
from config import Config

# Import blueprints
from users import users_blueprint
from donations import donations_blueprint
from projects import projects_blueprint

# Initialize app
app = Flask(__name__)
app.config.from_object(Config)

# Initialize database and migration
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Initialize session
Session(app)

# Register blueprints
app.register_blueprint(users_blueprint, url_prefix='/users')
app.register_blueprint(donations_blueprint, url_prefix='/donations')
app.register_blueprint(projects_blueprint, url_prefix='/projects')

@app.route('/')
def home():
    return "Welcome to the Blockchain-Based Donation Platform!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
