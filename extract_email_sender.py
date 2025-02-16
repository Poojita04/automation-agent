import re

# File paths
input_file = "/data/email.txt"
output_file = "/data/email-sender.txt"

# Read the email file
with open(input_file, "r", encoding="utf-8") as f:
    email_content = f.read()

# Updated regex to capture email inside <>
match = re.search(r'From: .*?<(.*?)>', email_content)

# Extract and save the email address
if match:
    sender_email = match.group(1)
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(sender_email + "\n")
    print(f"Extracted sender's email: {sender_email}")
else:
    print("No email address found in the provided content.")
