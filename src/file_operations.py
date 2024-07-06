import json

FILE_PATH = "../data/debt_balances.json"

# Load balances from JSON file to access entries
def load_balances(file_path):

    try:
        with open(file_path, "r") as file:
            entries = json.load(file)
        return entries
    except FileNotFoundError:
        print("File not found. Please check if debt_balances.json file exists")
        return[]
    except json.JSONDecodeError:
        print(f"Decoding error detected in balance database (JSON file): {e}")
        return []
    except Exception as e:
        print(f"Unexpected error occured: {e}")
        return[]

# Save a new balance/entry into the JSON file
def save_balance(file_path, entries):
    try:
        with open(file_path, "w") as file:
            json.dump(entries, file, indent=4)
    except Exception as e:
        print(f"Error. Entry failed to save: {e}")