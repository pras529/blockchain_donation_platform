import hashlib

def hash_data(data):
    return hashlib.sha256(data.encode()).hexdigest()

def validate_data(data):
    if not data:
        raise ValueError("Invalid data")
    return True
