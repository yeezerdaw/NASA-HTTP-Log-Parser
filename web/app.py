from flask import Flask, request, render_template, jsonify
import pickle
import os
import pandas as pd
import re
from collections import Counter

# Initialize Flask app
app = Flask(__name__)

# Configure the upload folder and allowed extensions
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['ALLOWED_EXTENSIONS'] = {'txt', 'log', 'csv'}

# Function to check if the uploaded file has an allowed extension
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# Path to the model
model_path = os.path.join(os.path.dirname(os.getcwd()), 'scripts/ml_model/error_classifier_model.pkl')

# Load the model
try:
    model = pickle.load(open(model_path, 'rb'))
except FileNotFoundError:
    raise Exception(f"Model file not found at {model_path}")

# Define routes

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    if file and allowed_file(file.filename):
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)
        return f'File uploaded successfully: {filename}'
    else:
        return 'Invalid file format'

# Define a regex pattern for parsing log lines
log_pattern = r'(?P<ip>\S+) - - \[(?P<date>.*?)\] "(?P<method>\S+) (?P<url>\S+) \S+" (?P<status>\d+) (?P<size>\d+)'

def parse_log_line(line):
    """Parse a single line from the log file using regex."""
    match = re.match(log_pattern, line)
    if match:
        return match.groupdict()
    return None

def classify_error(status_code):
    """Classify errors based on the HTTP status code."""
    if status_code == '404':
        return '404 Not Found'
    elif status_code == '403':
        return '403 Forbidden'
    elif status_code.startswith('4'):
        return 'Other Client Error'
    elif status_code == '500':
        return '500 Internal Server Error'
    elif status_code == '502':
        return '502 Bad Gateway'
    elif status_code.startswith('5'):
        return 'Other Server Error'
    else:
        return 'Successful'

@app.route('/parse_log', methods=['POST'])
def parse_log():
    file = request.files['file']
    log_data = []

    # Process the file
    for line in file:
        line = line.decode('utf-8')  # Convert binary file to string
        log_entry = parse_log_line(line)
        if log_entry:
            error_type = classify_error(log_entry['status'])
            log_data.append({
                'ip': log_entry['ip'],
                'url': log_entry['url'],
                'status': log_entry['status'],
                'error_type': error_type
            })

    # Convert data into DataFrame for model prediction
    df = pd.DataFrame(log_data)
    predictions = model.predict(df)

    # Return prediction results
    return jsonify(predictions.tolist())

if __name__ == '__main__':
    app.run(debug=True)
