from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import json
import os
from datetime import datetime
import uuid

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# In-memory storage for demo (use a real database in production)
users_data = {}
leaderboard_data = []

# Load dummy data
def load_dummy_data():
    dummy_users = [
        {
            "id": "1",
            "name": "Alex Johnson",
            "email": "alex@email.com",
            "referral_code": "alex2025",
            "total_donations": 5670,
            "rank": 1,
            "achievements": ["Bronze", "Silver", "Gold"]
        },
        {
            "id": "2", 
            "name": "Sarah Chen",
            "email": "sarah@email.com",
            "referral_code": "sarah2025",
            "total_donations": 4230,
            "rank": 2,
            "achievements": ["Bronze", "Silver"]
        },
        {
            "id": "3",
            "name": "Maya Patel", 
            "email": "maya@email.com",
            "referral_code": "maya2025",
            "total_donations": 3890,
            "rank": 3,
            "achievements": ["Bronze", "Silver"]
        },
        {
            "id": "4",
            "name": "David Kim",
            "email": "david@email.com", 
            "referral_code": "david2025",
            "total_donations": 2980,
            "rank": 5,
            "achievements": ["Bronze"]
        },
        {
            "id": "5",
            "name": "Emma Wilson",
            "email": "emma@email.com",
            "referral_code": "emma2025", 
            "total_donations": 2750,
            "rank": 6,
            "achievements": ["Bronze"]
        }
    ]
    
    for user in dummy_users:
        users_data[user["id"]] = user
    
    return dummy_users

# Initialize dummy data
load_dummy_data()

# Routes
@app.route('/')
def home():
    return jsonify({
        "message": "Intern Portal API", 
        "version": "1.0",
        "endpoints": [
            "/api/auth/login",
            "/api/auth/signup", 
            "/api/user/dashboard",
            "/api/leaderboard"
        ]
    })

# Authentication Routes
@app.route('/api/auth/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')
        
        if not email or not password:
            return jsonify({"error": "Email and password required"}), 400
        
        # Find user by email (in real app, verify password hash)
        user = None
        for user_data in users_data.values():
            if user_data.get('email') == email:
                user = user_data
                break
        
        if not user:
            # Create demo user for any email
            user_id = str(uuid.uuid4())
            name = email.split('@')[0].title()
            referral_code = f"{email.split('@')[0]}{datetime.now().year}"
            
            user = {
                "id": user_id,
                "name": name,
                "email": email,
                "referral_code": referral_code,
                "total_donations": 3350,
                "rank": 4,
                "achievements": ["Bronze", "Silver"]
            }
            users_data[user_id] = user
        
        return jsonify({
            "success": True,
            "message": "Login successful",
            "user": user
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/auth/signup', methods=['POST'])
def signup():
    try:
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')
        
        if not name or not email or not password:
            return jsonify({"error": "Name, email and password required"}), 400
        
        # Check if user already exists
        for user_data in users_data.values():
            if user_data.get('email') == email:
                return jsonify({"error": "User already exists"}), 400
        
        # Create new user
        user_id = str(uuid.uuid4())
        referral_code = f"{name.lower().replace(' ', '')}{datetime.now().year}"
        
        user = {
            "id": user_id,
            "name": name,
            "email": email,
            "referral_code": referral_code,
            "total_donations": 0,
            "rank": len(users_data) + 1,
            "achievements": []
        }
        
        users_data[user_id] = user
        
        return jsonify({
            "success": True,
            "message": "Signup successful",
            "user": user
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Dashboard Routes
@app.route('/api/user/dashboard', methods=['GET'])
def get_dashboard():
    try:
        # In real app, get user_id from JWT token
        user_id = request.args.get('user_id', '4')  # Default to demo user
        
        user = users_data.get(user_id)
        if not user:
            return jsonify({"error": "User not found"}), 404
        
        # Calculate achievements based on donations
        achievements = []
        if user["total_donations"] >= 1000:
            achievements.append("Bronze")
        if user["total_donations"] >= 2500:
            achievements.append("Silver") 
        if user["total_donations"] >= 5000:
            achievements.append("Gold")
        if user["total_donations"] >= 10000:
            achievements.append("Diamond")
        
        user["achievements"] = achievements
        
        return jsonify({
            "success": True,
            "user": user,
            "next_goal": 5000,
            "progress_percentage": min((user["total_donations"] / 5000) * 100, 100)
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/leaderboard', methods=['GET'])
def get_leaderboard():
    try:
        # Sort users by total donations
        sorted_users = sorted(users_data.values(), 
                            key=lambda x: x["total_donations"], 
                            reverse=True)
        
        # Update ranks
        for i, user in enumerate(sorted_users):
            user["rank"] = i + 1
        
        return jsonify({
            "success": True,
            "leaderboard": sorted_users[:10],  # Top 10
            "total_users": len(users_data)
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Health check
@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "users_count": len(users_data)
    })

if __name__ == '__main__':
    print("🚀 Starting Intern Portal API...")
    print("📊 Loaded dummy data for", len(users_data), "users")
    print("🌐 API will be available at: http://localhost:5000")
    
    app.run(
        debug=True,
        host='0.0.0.0',
        port=5000
    )