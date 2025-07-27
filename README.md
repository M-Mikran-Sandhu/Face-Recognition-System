# Face Recognition System

A modern, sleek face recognition system built with Flask (Python) backend and React frontend. This system provides secure authentication using advanced facial recognition technology powered by MediaPipe.

## Features

- **User Registration**: Register new users with facial data
- **Face Recognition**: Authenticate users using facial recognition
- **User Management**: View and manage registered users
- **Modern UI/UX**: Sleek, responsive design with gradient backgrounds and smooth animations
- **Real-time Camera**: Live camera feed for face capture
- **Cross-platform**: Works on desktop and mobile devices

## Technology Stack

### Backend
- **Flask**: Python web framework
- **MediaPipe**: Google's machine learning framework for face detection
- **OpenCV**: Computer vision library for image processing
- **SQLite**: Database for user management (optional)
- **Flask-CORS**: Cross-origin resource sharing support

### Frontend
- **React**: Modern JavaScript framework
- **Tailwind CSS**: Utility-first CSS framework
- **shadcn/ui**: High-quality UI components
- **Lucide Icons**: Beautiful icon library
- **Vite**: Fast build tool and development server

## Installation and Setup

### Prerequisites
- Python 3.10+
- Node.js 18+
- Camera/Webcam access

### Backend Setup

1. Navigate to the project directory:
   ```bash
   cd face-recognition-system
   ```

2. Create and activate virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Flask server:
   ```bash
   python src/main.py
   ```

The backend will be available at `http://localhost:5000`

### Frontend Setup (Development)

1. Navigate to the frontend directory:
   ```bash
   cd face-recognition-frontend
   ```

2. Install dependencies:
   ```bash
   pnpm install
   ```

3. Start the development server:
   ```bash
   pnpm run dev
   ```

The frontend will be available at `http://localhost:5173`

### Production Deployment

The project is configured for full-stack deployment where the Flask backend serves the built React frontend:

1. Build the React frontend:
   ```bash
   cd face-recognition-frontend
   pnpm run build
   ```

2. Copy built files to Flask static directory:
   ```bash
   cp -r dist/* ../face-recognition-system/src/static/
   ```

3. Run the Flask server:
   ```bash
   cd face-recognition-system
   source venv/bin/activate
   python src/main.py
   ```

The complete application will be available at `http://localhost:5000`

## API Endpoints

### Face Recognition API

- `POST /api/face/register` - Register a new user with face data
- `POST /api/face/recognize` - Recognize a face and authenticate user
- `POST /api/face/detect` - Detect faces in an image
- `GET /api/face/users` - Get list of registered users
- `DELETE /api/face/users/<username>` - Delete a registered user

### Request/Response Examples

#### Register User
```json
POST /api/face/register
{
  "username": "john_doe",
  "image": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQ..."
}
```

#### Recognize Face
```json
POST /api/face/recognize
{
  "image": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQ..."
}

Response:
{
  "recognized": true,
  "username": "john_doe",
  "confidence": 0.85
}
```

## Usage

1. **Register a New User**:
   - Go to the "Register" tab
   - Enter a username
   - Click "Start Camera" to begin face capture
   - Click "Capture" when ready
   - Click "Register Face" to save the user

2. **Recognize a Face**:
   - Go to the "Recognize" tab
   - Click "Start Camera" to begin face capture
   - Click "Capture" when ready
   - Click "Recognize Face" to authenticate

3. **Manage Users**:
   - Go to the "Users" tab
   - View all registered users
   - Delete users as needed

## Project Structure

```
face-recognition-system/
├── src/
│   ├── routes/
│   │   ├── face_recognition.py    # Face recognition API routes
│   │   └── user.py               # User management routes
│   ├── models/
│   │   └── user.py               # Database models
│   ├── static/                   # Built React frontend files
│   ├── face_data/               # Stored face recognition data
│   └── main.py                  # Flask application entry point
├── venv/                        # Python virtual environment
├── requirements.txt             # Python dependencies
└── README.md                   # This file

face-recognition-frontend/
├── src/
│   ├── components/              # React components
│   ├── assets/                  # Static assets
│   ├── App.jsx                  # Main React component
│   └── main.jsx                 # React entry point
├── dist/                        # Built frontend files
├── package.json                 # Node.js dependencies
└── vite.config.js              # Vite configuration
```

## Security Considerations

- Face data is stored as feature vectors, not actual images
- CORS is enabled for development but should be configured for production
- Consider implementing rate limiting for API endpoints
- Use HTTPS in production environments
- Implement proper authentication and authorization for admin functions

## Browser Compatibility

- Chrome 60+
- Firefox 55+
- Safari 11+
- Edge 79+

Camera access requires HTTPS in production environments.

## Troubleshooting

### Common Issues

1. **Camera not working**: Ensure camera permissions are granted and HTTPS is used in production
2. **Face not detected**: Ensure good lighting and face is clearly visible
3. **Recognition accuracy**: Multiple face samples per user can improve accuracy
4. **CORS errors**: Check that Flask-CORS is properly configured

### Development Tips

- Use good lighting for better face detection
- Capture multiple angles during registration for better recognition
- Test with different users to validate system performance
- Monitor browser console for any JavaScript errors

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the MIT License.

## Acknowledgments

- MediaPipe by Google for face detection capabilities
- React and Tailwind CSS communities for excellent documentation
- shadcn/ui for beautiful, accessible UI components

