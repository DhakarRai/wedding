from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

# Configure static files path
@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

# Main route
@app.route('/')
def home():
    return render_template('wed.html')

# Error handling
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)