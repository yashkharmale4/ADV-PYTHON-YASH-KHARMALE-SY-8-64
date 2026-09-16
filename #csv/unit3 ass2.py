import csv
import json

# Step 1: Import the required modules

# Step 2: Specify the input CSV file
input_file = "students.csv"

# Step 3: Specify the output JSON file
output_file = "students.json"

# Step 4: Open the CSV file in read mode
with open(input_file, "r", newline="") as csv_file:
    csv_reader = csv.DictReader(csv_file)

    # Convert CSV data into a list of dictionaries
    data = list(csv_reader)

# Step 5: Write the data into a JSON file
with open(output_file, "w") as json_file:
    json.dump(data, json_file, indent=4)

print("CSV file converted to JSON successfully!")