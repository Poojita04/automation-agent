from datetime import datetime

# Open and read the file
with open("D:/TDS/automation-agent/data/date.txt", "r", encoding="utf-8-sig") as file:
    dates = file.readlines()

# Count Wednesdays
wednesday_count = sum(1 for date in dates if datetime.strptime(date.strip(), "%Y-%m-%d").weekday() == 2)

print(f"Number of Wednesdays: {wednesday_count}")
