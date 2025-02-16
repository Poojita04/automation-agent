import os
import glob

# File paths
log_dir = "/data/logs/"
output_file = "/data/logs-recent.txt"

# Find all .log files in the directory
log_files = glob.glob(os.path.join(log_dir, "*.log"))

# Sort by last modified time (most recent first)
log_files.sort(key=os.path.getmtime, reverse=True)

# Extract first line from the 10 most recent log files
recent_lines = []
for log_file in log_files[:10]:  # Get up to 10 most recent files
    with open(log_file, "r", encoding="utf-8") as f:
        first_line = f.readline().strip()  # Read first line and remove extra spaces
        recent_lines.append(first_line)

# Write to output file
with open(output_file, "w", encoding="utf-8") as f:
    f.write("\n".join(recent_lines) + "\n")

print(f"Extracted first lines from {len(recent_lines)} log files to {output_file}")
