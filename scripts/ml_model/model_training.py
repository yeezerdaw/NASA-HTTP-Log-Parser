import re
import pandas as pd
from collections import Counter

# Define the log line regex pattern
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

def extract_features(file_path):
    """Extract features from the log file for ML training."""
    ip_counter = Counter()
    url_counter = Counter()
    status_counter = Counter()
    timestamp_counter = Counter()
    error_classification = Counter()

    data = []

    with open(file_path, 'r', encoding='ISO-8859-1') as f:
        for line in f:
            log_data = parse_log_line(line)
            if log_data:
                ip_counter[log_data['ip']] += 1
                url_counter[log_data['url']] += 1
                status_counter[log_data['status']] += 1
                timestamp_counter[log_data['date']] += 1
                error_type = classify_error(log_data['status'])
                error_classification[error_type] += 1

                # Create a feature row
                data.append({
                    'ip': log_data['ip'],
                    'url': log_data['url'],
                    'status': log_data['status'],
                    'timestamp': log_data['date'],
                    'error_type': error_type
                })

    # Convert to a pandas DataFrame for ML
    df = pd.DataFrame(data)

    # Add additional features for frequency of IPs and URLs
    df['ip_frequency'] = df['ip'].apply(lambda x: ip_counter[x])
    df['url_frequency'] = df['url'].apply(lambda x: url_counter[x])
    df['status_frequency'] = df['status'].apply(lambda x: status_counter[x])
    df['timestamp_frequency'] = df['timestamp'].apply(lambda x: timestamp_counter[x])

    return df

# Example usage: Generate dataset for ML
file_path = '/home/yeshwanthk014/LogAnalysis/scripts/nasa-http-access-logs/access.log' # Replace with your actual log file path
df = extract_features(file_path)

# Save the DataFrame as a CSV file for training the model
df.to_csv('log_features.csv', index=False)
print("Features extracted and saved to 'log_features.csv'.")

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import pandas as pd

# Load the feature dataset (CSV file generated from the previous code)
df = pd.read_csv('log_features.csv')

# Define features (X) and target variable (y)
X = df[['ip_frequency', 'url_frequency', 'status_frequency', 'timestamp_frequency']]
y = df['error_type']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize the Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the model
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
print(classification_report(y_test, y_pred))

# Save the trained model using joblib for later inference
import joblib
joblib.dump(model, 'error_classifier_model.pkl')

print("Model trained and saved as 'error_classifier_model.pkl'")
