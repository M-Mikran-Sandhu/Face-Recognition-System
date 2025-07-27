# Installation Guide

This guide will help you set up the Face Recognition System on your local machine.

## System Requirements

- **Operating System**: Windows 10+, macOS 10.14+, or Linux (Ubuntu 18.04+)
- **Python**: 3.10 or higher
- **Node.js**: 18.0 or higher (for frontend development)
- **Camera**: Webcam or built-in camera
- **RAM**: Minimum 4GB, recommended 8GB+
- **Storage**: At least 2GB free space

## Quick Start (Production Ready)

If you just want to run the complete application:

1. **Extract the project files**:
   ```bash
   unzip face-recognition-system.zip
   cd face-recognition-system
   ```

2. **Set up Python environment**:
   ```bash
   python -m venv venv
   
   # On Windows:
   venv\Scripts\activate
   
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```bash
   python src/main.py
   ```

5. **Open your browser** and go to `http://localhost:5000`

That's it! The application is now running with the pre-built frontend.

## Development Setup

If you want to modify the frontend or work on development:

### Backend Setup

1. **Navigate to backend directory**:
   ```bash
   cd face-recognition-system
   ```

2. **Create virtual environment**:
   ```bash
   python -m venv venv
   ```

3. **Activate virtual environment**:
   ```bash
   # Windows
   venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
   ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Run Flask server**:
   ```bash
   python src/main.py
   ```

### Frontend Setup (for development)

1. **Navigate to frontend directory**:
   ```bash
   cd face-recognition-frontend
   ```

2. **Install Node.js dependencies**:
   ```bash
   # Using pnpm (recommended)
   pnpm install
   
   # Or using npm
   npm install
   ```

3. **Start development server**:
   ```bash
   # Using pnpm
   pnpm run dev
   
   # Or using npm
   npm run dev
   ```

4. **Open browser** to `http://localhost:5173` for development

## Platform-Specific Instructions

### Windows

1. **Install Python**:
   - Download from [python.org](https://www.python.org/downloads/)
   - Make sure to check "Add Python to PATH" during installation

2. **Install Node.js** (for development):
   - Download from [nodejs.org](https://nodejs.org/)

3. **Install Visual C++ Build Tools** (if needed):
   - Download "Microsoft C++ Build Tools" if you encounter compilation errors

### macOS

1. **Install Python**:
   ```bash
   # Using Homebrew
   brew install python@3.11
   ```

2. **Install Node.js** (for development):
   ```bash
   # Using Homebrew
   brew install node
   ```

### Linux (Ubuntu/Debian)

1. **Install Python and pip**:
   ```bash
   sudo apt update
   sudo apt install python3.11 python3.11-venv python3-pip
   ```

2. **Install build essentials**:
   ```bash
   sudo apt install build-essential cmake
   ```

3. **Install Node.js** (for development):
   ```bash
   # Using NodeSource repository
   curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
   sudo apt-get install -y nodejs
   ```

## Troubleshooting Installation

### Python Issues

**Problem**: `python` command not found
**Solution**: 
- On Windows: Use `py` instead of `python`
- On macOS/Linux: Use `python3` instead of `python`

**Problem**: Permission denied when installing packages
**Solution**: 
- Make sure virtual environment is activated
- On Linux/macOS: Don't use `sudo` with pip in virtual environment

**Problem**: CMake not found during installation
**Solution**:
- Windows: Install Visual Studio Build Tools
- macOS: Install Xcode command line tools: `xcode-select --install`
- Linux: Install cmake: `sudo apt install cmake build-essential`

### Camera Issues

**Problem**: Camera not accessible
**Solution**:
- Check browser permissions for camera access
- Ensure no other applications are using the camera
- Use HTTPS in production (required for camera access)

**Problem**: Camera shows black screen
**Solution**:
- Try refreshing the page
- Check if camera drivers are installed
- Test camera in other applications

### Network Issues

**Problem**: CORS errors when accessing API
**Solution**:
- Ensure Flask-CORS is installed: `pip install flask-cors`
- Check that CORS is enabled in the Flask app
- For development, both frontend and backend should be running

**Problem**: Cannot access application from other devices
**Solution**:
- Flask runs on `0.0.0.0:5000` by default (accessible from network)
- Check firewall settings
- Ensure devices are on the same network

## Performance Optimization

### For Better Face Recognition

1. **Lighting**: Ensure good, even lighting on the face
2. **Camera Quality**: Use a higher resolution camera if available
3. **Multiple Samples**: Register multiple face samples per user
4. **Stable Position**: Keep face steady during capture

### For Better Performance

1. **Close Unnecessary Applications**: Free up RAM and CPU
2. **Use Chrome/Edge**: Generally better WebRTC support
3. **Wired Connection**: Use ethernet instead of WiFi if possible
4. **Update Drivers**: Ensure camera drivers are up to date

## Security Setup

### For Production Deployment

1. **Use HTTPS**: Required for camera access in production
2. **Configure CORS**: Restrict origins in production
3. **Environment Variables**: Use environment variables for secrets
4. **Firewall**: Configure firewall rules appropriately
5. **Regular Updates**: Keep dependencies updated

### Example Production Configuration

```python
# In src/main.py for production
import os

if __name__ == '__main__':
    # Use environment variables
    host = os.getenv('HOST', '0.0.0.0')
    port = int(os.getenv('PORT', 5000))
    debug = os.getenv('DEBUG', 'False').lower() == 'true'
    
    app.run(host=host, port=port, debug=debug)
```

## Getting Help

If you encounter issues:

1. **Check the logs**: Look at the terminal output for error messages
2. **Browser Console**: Check browser developer tools for JavaScript errors
3. **Dependencies**: Ensure all requirements are installed correctly
4. **Permissions**: Verify camera and file permissions
5. **Documentation**: Refer to the main README.md for usage instructions

## Next Steps

After successful installation:

1. **Test the System**: Try registering a user and recognizing faces
2. **Explore Features**: Test all three tabs (Register, Recognize, Users)
3. **Customize**: Modify the code to fit your specific needs
4. **Deploy**: Consider deployment options for production use

For detailed usage instructions, see the main README.md file.

