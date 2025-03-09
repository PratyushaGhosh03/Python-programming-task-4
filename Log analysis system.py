import re
from collections import Counter

def parse_log(file_path):
    ip_counter = Counter()
    status_counter = Counter()
    
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.split()
            if len(parts) > 6:
                ip = parts[0]  # Extract IP address
                status = parts[-2]  # Extract HTTP status code
                ip_counter[ip] += 1
                status_counter[status] += 1
    
    print("Most frequent IPs:", ip_counter.most_common(5))
    print("Response code counts:", status_counter)

# Example usage:
# parse_log('access.log')
