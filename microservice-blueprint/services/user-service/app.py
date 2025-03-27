from flask import Flask, jsonify
import logging
import os

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Sample users data
users = [
    {"id": 1, "name": "John Doe", "email": "john.doe@example.com", "role": "Developer"},
    {"id": 2, "name": "Jane Smith", "email": "jane.smith@example.com", "role": "Manager"},
    {"id": 3, "name": "Bob Johnson", "email": "bob.johnson@example.com", "role": "Designer"}
]

@app.route('/users')
def get_users():
    """
    Endpoint to retrieve all users
    """
    logger.info("Fetching all users")
    return jsonify(users)

@app.route('/users/<int:user_id>')
def get_user(user_id):
    """
    Endpoint to retrieve a specific user by ID
    """
    user = next((user for user in users if user['id'] == user_id), None)
    
    if user:
        logger.info(f"Fetched user with ID: {user_id}")
        return jsonify(user)
    else:
        logger.warning(f"User with ID {user_id} not found")
        return jsonify({"error": "User not found"}), 404

@app.route('/health')
def health_check():
    """
    Health check endpoint
    """
    return jsonify({
        "status": "healthy",
        "service": "user-service",
        "version": "1.0.0"
    })

if __name__ == '__main__':
    # Use port from environment variable or default to 5000
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
