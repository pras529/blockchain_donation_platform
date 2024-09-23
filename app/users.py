from flask import Blueprint, request, jsonify, session
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import User, Donor, Charity
from app import db

users_blueprint = Blueprint('users', __name__)


# User Registration
@users_blueprint.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()

    # Check if user already exists
    existing_user = User.query.filter_by(email=data['email']).first()
    if existing_user:
        return jsonify({'message': 'User already exists.'}), 409

    # Hash password
    hashed_password = generate_password_hash(data['password'], method='sha256')

    # Create new user
    new_user = User(
        username=data['username'],
        email=data['email'],
        password=hashed_password,
        role=data['role']  # 'donor' or 'charity'
    )
    db.session.add(new_user)
    db.session.commit()

    if data['role'] == 'donor':
        donor = Donor(user_id=new_user.id)
        db.session.add(donor)
    elif data['role'] == 'charity':
        charity = Charity(user_id=new_user.id)
        db.session.add(charity)

    db.session.commit()
    return jsonify({'message': 'User registered successfully.'}), 201


# User Login
@users_blueprint.route('/login', methods=['POST'])
def login_user():
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()

    # Verify user
    if not user or not check_password_hash(user.password, data['password']):
        return jsonify({'message': 'Invalid email or password.'}), 401

    # Save user to session
    session['user_id'] = user.id
    session['role'] = user.role
    return jsonify({'message': 'Login successful.', 'role': user.role}), 200


# Logout User
@users_blueprint.route('/logout', methods=['POST'])
def logout_user():
    session.pop('user_id', None)
    session.pop('role', None)
    return jsonify({'message': 'Logout successful.'}), 200


# Get User Profile (Donor or Charity)
@users_blueprint.route('/profile', methods=['GET'])
def get_user_profile():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({'message': 'Unauthorized.'}), 401

    user = User.query.get(user_id)
    if user.role == 'donor':
        donor_profile = Donor.query.filter_by(user_id=user_id).first()
        profile_data = {
            'username': user.username,
            'email': user.email,
            'donated_projects': [donation.project.name for donation in donor_profile.donations]
        }
    elif user.role == 'charity':
        charity_profile = Charity.query.filter_by(user_id=user_id).first()
        profile_data = {
            'username': user.username,
            'email': user.email,
            'projects': [project.name for project in charity_profile.projects]
        }
    else:
        profile_data = {}

    return jsonify({'profile': profile_data}), 200


# Update User Profile
@users_blueprint.route('/profile', methods=['PUT'])
def update_user_profile():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({'message': 'Unauthorized.'}), 401

    data = request.get_json()
    user = User.query.get(user_id)

    # Update fields
    user.username = data.get('username', user.username)
    if data.get('password'):
        user.password = generate_password_hash(data['password'], method='sha256')

    db.session.commit()
    return jsonify({'message': 'Profile updated successfully.'}), 200


# Delete User
@users_blueprint.route('/delete', methods=['DELETE'])
def delete_user():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({'message': 'Unauthorized.'}), 401

    user = User.query.get(user_id)
    db.session.delete(user)
    db.session.commit()

    session.pop('user_id', None)
    session.pop('role', None)

    return jsonify({'message': 'User account deleted.'}), 200
