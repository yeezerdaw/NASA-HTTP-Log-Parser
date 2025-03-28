import re
from collections import Counter

# Define a regex pattern to capture relevant parts of the log line
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
        return 'Other'

def process_logs(file_path):
    """Process the log file, count URLs, IPs, status codes, and classify errors."""
    url_counter = Counter()
    status_counter = Counter()
    ip_counter = Counter()
    error_classification = Counter()

    # Open the log file with the correct encoding to handle non-UTF-8 characters
    with open(file_path, 'r', encoding='ISO-8859-1') as f:  # Use ISO-8859-1 encoding
        for line in f:
            log_data = parse_log_line(line)
            if log_data:
                # Count the URLs, status codes, and IPs
                url_counter[log_data['url']] += 1
                status_counter[log_data['status']] += 1
                ip_counter[log_data['ip']] += 1
                
                # Classify errors based on the status code
                error_type = classify_error(log_data['status'])
                error_classification[error_type] += 1

    # Display results
    print("Most requested URLs:")
    for url, count in url_counter.most_common(5):
        print(f"{url}: {count}")

    print("\nStatus codes count:")
    for status, count in status_counter.items():
        print(f"{status}: {count}")

    print("\nMost active IPs:")
    for ip, count in ip_counter.most_common(5):
        print(f"{ip}: {count}")

    print("\nError Classification:")
    for error_type, count in error_classification.items():
        print(f"{error_type}: {count}")

# Example usage
process_logs('/home/yeshwanthk014/LogAnalysis/scripts/nasa-http-access-logs/access.log')
