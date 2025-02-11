import os
import json
import pandas as pd



JSON_FILE = "results.json"
CSV_FILE = "results.csv"

def json_to_csv():
    if os.path.exists(JSON_FILE):
        try:
            with open(JSON_FILE, "r") as file:
                data = json.load(file)

            df = pd.DataFrame(data)
            df.to_csv(CSV_FILE, index=False)

            print(f"Converted: {JSON_FILE} → {CSV_FILE}")
        except Exception as e:
            print(f"Error processing {JSON_FILE}: {e}")
    else:
        print("JSON file not found.")

if __name__ == "__main__":
    json_to_csv()

###############################################################################################################################
#In case you dont want to automate the conversion of JSON to CSV, you can use the following code to convert JSON to CSV
#   You'll need to run this script manually after running image_processing.py to generate the results.json file.
#   !!!!!!!!!! You will have to delete on image_processing.py
#                            !!!       1-   the line that contains    "import subprocess"                               !!!
#                            !!!       2-   the line that contains    "subprocess.run(["python", "json_to_csv.py"])"    !!!

#################### BEGENNING OF THE CODE ####################################################################################

# import json
# import csv

# # Read JSON file
# with open("results.json", "r") as json_file:
#     json_data = json.load(json_file)

# # Convert JSON to CSV
# csv_file = "results.csv"

# with open(csv_file, "w", newline="") as file:
#     writer = csv.DictWriter(file, fieldnames=json_data[0].keys())
#     writer.writeheader()
#     writer.writerows(json_data)

# print("CSV file created successfully.")