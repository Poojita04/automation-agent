import os
import glob
import json

# File paths
docs_dir = "/data/docs/"
output_file = "/data/docs/index.json"

# Find all Markdown files
md_files = glob.glob(os.path.join(docs_dir, "*.md"))

# Dictionary to store file-title mappings
index = {}

# Process each Markdown file
for md_file in md_files:
    with open(md_file, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line.startswith("# "):  # Found the first H1
                filename = os.path.basename(md_file)  # Get filename only
                index[filename] = line[2:]  # Store title without "# "
                break  # Stop reading after the first H1

# Save the index as a JSON file
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(index, f, indent=4)

print(f"Extracted titles from {len(index)} files and saved to {output_file}")
