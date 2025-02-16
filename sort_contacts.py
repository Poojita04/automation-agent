import json

# File paths
input_file = "/data/contacts.json"
output_file = "/data/contacts-sorted.json"

# Load contacts data
with open(input_file, "r", encoding="utf-8") as f:
    contacts = json.load(f)

# Sort contacts by last_name, then first_name
contacts_sorted = sorted(contacts, key=lambda x: (x["last_name"], x["first_name"]))

# Save sorted contacts
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(contacts_sorted, f, indent=4)

print(f"Sorted contacts saved to {output_file}")
