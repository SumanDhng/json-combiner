import os
import json
import pandas as pd

# Initialize an empty list
json_data = []
json_folder = input("Folder Path:")

# Walk through the directory
for root,dirs, files in os.walk(json_folder):
    for file in files:
        # Check if the file is a JSON file
        if file.endswith('.json'):
            print(root,file)
            file_path = os.path.join(root,file)

            # Open and load the JSON data
            with open(file_path, 'r') as json_file:
                json_individual = json.load(json_file)
                
            # Store the individual JSON data along with the file name
            json_individual = {
                "file_name": file,
                "json": json_individual 
            }
            json_data.append(json_individual)

# Write the combined JSON data to an output JSON file
with open("json_combined.json", "w") as json_file:
    json.dump(json_data, json_file, indent=4)

# Read the data from the output JSON file
with open("json_combined.json" ,"r") as json_file:
    json_data = json.load(json_file)

# Data Conversion
df = pd.DataFrame.from_dict(json_data)
df.to_excel('combined_output.xlsx', index=False)
