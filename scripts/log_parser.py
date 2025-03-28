import os

# Define the path to the log file
log_file_path = os.path.expanduser('~/LogAnalysis/datasets/nasa-http-access-logs/access.log')

# Function to parse the log file and return a list of log entries
def parse_log_file(file_path):
    log_entries = []
    with open(file_path, 'r') as file:
        for line in file:
            log_entries.append(line.strip())
    return log_entries

# Parse the log file and print the first 10 entries
if __name__ == "__main__":
    log_entries = parse_log_file(log_file_path)
    for i, entry in enumerate(log_entries[:10]):
        print(f"{i+1}: {entry}")
