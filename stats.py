import json
import matplotlib.pyplot as plt
from collections import defaultdict

data_file = r"C:\Users\felix\Downloads\Quick Share\localStorage-backup (5).json"

# Parse data
data = json.load(open(data_file, "r", encoding="utf-8"))

# Extract raw numbers
attend_nums = {}

for key, value in data.items():
    if key.startswith("num ") and value != "0":
        attend_nums[key[4:]] = int(value)

# Sort by value
attend_nums = dict(sorted(attend_nums.items(), key=lambda item: item[1], reverse=True))



college_entries = {}
names = {}
name_list = []

for key, value in data.items():
    if key.startswith("barData "):

        # Convert JSON string to Python object
        value = json.loads(value)


        college_name = key.replace("barData ", "")
        college_entries[college_name] = value

        # Add names to list
        for entry in value:
            names_in_entry = []
            # Separate names
            if "," in entry["whoWith"]:
                names_in_entry = entry["whoWith"].split(", ")
            else:
                names_in_entry = [entry["whoWith"]]

            name_list.append(names_in_entry)
            
# Collapse name list
name_list = [name for sublist in name_list for name in sublist]


# Count names
for name in name_list:
    if name in names:
        names[name] += 1
    else:
        names[name] = 1


# Bar chart of attendance numbers
plt.figure(figsize=(10, 5))
plt.bar(attend_nums.keys(), attend_nums.values())
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Names bar chart
names = dict(sorted(names.items(), key=lambda item: item[1], reverse=True))
plt.figure(figsize=(10, 5))
plt.bar(names.keys(), names.values())
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()