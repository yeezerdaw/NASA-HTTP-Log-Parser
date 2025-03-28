import re

log_pattern = r'(?P<ip>\S+) - - \[(?P<date>.*?)\] "(?P<method>\S+) (?P<url>\S+) \S+" (?P<status>\d+) (?P<size>\d+)'

def parse_log_line(line):
    match = re.match(log_pattern, line)
    if match:
        return match.groupdict()
    return None

def classify_error(status_code):
    if status_code == '404':
        return '404 Not Found'
    elif status_code == '403':
        return '403 Forbidden'
    # Add more conditions for other status codes

