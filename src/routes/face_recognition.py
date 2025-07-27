from flask import Blueprint, request, jsonify
import cv2
import numpy as np
import mediapipe as mp
import base64
import io
from PIL import Image
import os
import json
from datetime import datetime
import threading

face_recognition_bp = Blueprint('face_recognition', __name__)

# Initialize MediaPipe Face Detection
mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

# Directory to store face encodings
FACE_DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'face_data')
os.makedirs(FACE_DATA_DIR, exist_ok=True)

def load_face_data():
    """Load face data from JSON file"""
    face_data_file = os.path.join(FACE_DATA_DIR, 'face_data.json')
    if os.path.exists(face_data_file):
        with open(face_data_file, 'r') as f:
            return json.load(f)
    return {}

def save_face_data(face_data):
    """Save face data to JSON file"""
    face_data_file = os.path.join(FACE_DATA_DIR, 'face_data.json')
    with open(face_data_file, 'w') as f:
        json.dump(face_data, f, indent=2)

def extract_face_features(image):
    """Extract face features using MediaPipe"""
    with mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.5) as face_detection:
        # Convert PIL image to OpenCV format
        image_cv = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        rgb_image = cv2.cvtColor(image_cv, cv2.COLOR_BGR2RGB)
        
        # Process the image
        results = face_detection.process(rgb_image)
        
        if results.detections:
            # For simplicity, we'll use the bounding box coordinates as features
            # In a real application, you'd use more sophisticated face encoding
            detection = results.detections[0]  # Use first detected face
            bbox = detection.location_data.relative_bounding_box
            
            # Create a simple feature vector from bounding box and confidence
            features = [
                bbox.xmin,
                bbox.ymin,
                bbox.width,
                bbox.height,
                detection.score[0]
            ]
            return features
        return None

def compare_faces(features1, features2, threshold=0.1):
    """Compare two face feature vectors"""
    if not features1 or not features2:
        return False
    
    # Simple Euclidean distance comparison
    distance = np.linalg.norm(np.array(features1) - np.array(features2))
    return distance < threshold

def get_next_id(face_data):
    if not face_data:
        return 1
    return max(int(user['id']) for user in face_data.values() if 'id' in user) + 1

# Add a lock for thread safety
face_data_lock = threading.Lock()

@face_recognition_bp.route('/register', methods=['POST'])
def register_face():
    """Register a new face"""
    try:
        data = request.get_json()
        username = data.get('username')
        image_data = data.get('image')
        if not username or not image_data:
            return jsonify({'error': 'Username and image are required'}), 400
        image_data = image_data.split(',')[1]  # Remove data:image/jpeg;base64, prefix
        image_bytes = base64.b64decode(image_data)
        image = Image.open(io.BytesIO(image_bytes))
        features = extract_face_features(image)
        if not features:
            return jsonify({'error': 'No face detected in the image'}), 400
        with face_data_lock:
            face_data = load_face_data()
            # Check if user already exists
            for user in face_data.values():
                if user['username'] == username:
                    return jsonify({'error': 'User already exists'}), 400
            user_id = get_next_id(face_data)
            face_data[str(user_id)] = {
                'id': user_id,
                'username': username,
                'features': features,
                'registered_at': datetime.now().isoformat()
            }
            save_face_data(face_data)
        return jsonify({'message': f'Face registered successfully for {username}', 'id': user_id}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@face_recognition_bp.route('/recognize', methods=['POST'])
def recognize_face():
    """Recognize a face"""
    try:
        data = request.get_json()
        image_data = data.get('image')
        
        if not image_data:
            return jsonify({'error': 'Image is required'}), 400
        
        # Decode base64 image
        image_data = image_data.split(',')[1]  # Remove data:image/jpeg;base64, prefix
        image_bytes = base64.b64decode(image_data)
        image = Image.open(io.BytesIO(image_bytes))
        
        # Extract face features
        features = extract_face_features(image)
        if not features:
            return jsonify({'error': 'No face detected in the image'}), 400
        
        # Load existing face data
        face_data = load_face_data()
        
        # Compare with registered faces
        best_match = None
        best_distance = float('inf')
        
        for username, user_data in face_data.items():
            stored_features = user_data['features']
            distance = np.linalg.norm(np.array(features) - np.array(stored_features))
            
            if distance < best_distance:
                best_distance = distance
                best_match = username
        
        # Check if match is good enough
        if best_match and best_distance < 0.1:  # Threshold for recognition
            return jsonify({
                'recognized': True,
                'username': best_match,
                'confidence': 1 - best_distance
            }), 200
        else:
            return jsonify({
                'recognized': False,
                'message': 'Face not recognized'
            }), 200
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@face_recognition_bp.route('/detect', methods=['POST'])
def detect_face():
    """Detect faces in an image"""
    try:
        data = request.get_json()
        image_data = data.get('image')
        
        if not image_data:
            return jsonify({'error': 'Image is required'}), 400
        
        # Decode base64 image
        image_data = image_data.split(',')[1]  # Remove data:image/jpeg;base64, prefix
        image_bytes = base64.b64decode(image_data)
        image = Image.open(io.BytesIO(image_bytes))
        
        # Convert to OpenCV format
        image_cv = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        rgb_image = cv2.cvtColor(image_cv, cv2.COLOR_BGR2RGB)
        
        # Detect faces
        with mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.5) as face_detection:
            results = face_detection.process(rgb_image)
            
            faces = []
            if results.detections:
                for detection in results.detections:
                    bbox = detection.location_data.relative_bounding_box
                    faces.append({
                        'x': bbox.xmin,
                        'y': bbox.ymin,
                        'width': bbox.width,
                        'height': bbox.height,
                        'confidence': detection.score[0]
                    })
            
            return jsonify({
                'faces_detected': len(faces),
                'faces': faces
            }), 200
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@face_recognition_bp.route('/users', methods=['GET'])
def get_users():
    """Get list of registered users"""
    try:
        face_data = load_face_data()
        users = []
        for user in face_data.values():
            users.append({
                'id': user.get('id'),
                'username': user.get('username'),
                'registered_at': user.get('registered_at', 'Unknown')
            })
        return jsonify({'users': users}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@face_recognition_bp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """Delete a registered user by id"""
    try:
        with face_data_lock:
            face_data = load_face_data()
            user_key = None
            for key, user in face_data.items():
                if user.get('id') == user_id:
                    user_key = key
                    break
            if user_key is None:
                return jsonify({'error': 'User not found'}), 404
            del face_data[user_key]
            save_face_data(face_data)
        return jsonify({'message': f'User with id {user_id} deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@face_recognition_bp.route('/users/clear', methods=['POST'])
def clear_all_faces():
    """Clear all registered faces"""
    try:
        with face_data_lock:
            save_face_data({})
        return jsonify({'message': 'All faces cleared successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

