import os

# Expanding the home directory to the full path
log_file_path = os.path.expanduser('~/LogAnalysis/datasets/nasa-http-access-logs/access.log')

# Open the file and print the first 10 lines
with open(log_file_path, 'r') as file:
    for i, line in enumerate(file):
        if i < 10:
            print(line.strip())  # Print the first 10 lines
        else:
            break
