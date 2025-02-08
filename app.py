from flask import Flask, render_template, send_from_directory, url_for
import os

app = Flask(__name__, static_folder='static')

# Configure custom static files path
@app.route('/static/<path:path>')
def serve_static(path):
    try:
        return send_from_directory('static', path)
    except Exception as e:
        app.logger.error(f"Error serving static file: {e}")
        return "File not found", 404

# Audio file route
@app.route('/static/audio/<path:filename>')
def serve_audio(filename):
    try:
        # Specify the correct path to your audio directory
        audio_dir = os.path.join(app.static_folder, 'audio')
        return send_from_directory(audio_dir, filename)
    except Exception as e:
        app.logger.error(f"Error serving audio file: {e}")
        return "Audio file not found", 404

# Main route
@app.route('/')
def home():
    try:
        # Generate the correct URL for the audio file
        audio_url = url_for('static', filename='audio/9.mp3')
        return render_template('wed.html', audio_url=audio_url)
    except Exception as e:
        app.logger.error(f"Error rendering template: {e}")
        return "Error loading page", 500

# Error handling
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    # Ensure static folders exist
    os.makedirs(os.path.join(app.static_folder, 'audio'), exist_ok=True)
    
    # Set host to '0.0.0.0' to make it accessible from other devices on the network
    app.run(debug=True)