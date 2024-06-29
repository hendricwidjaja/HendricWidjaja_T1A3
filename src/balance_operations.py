import json

# Load balances from JSON file to access entries
# Parameter = file_path: Path to JSON file containing entries
# Return: List of entries or an empty list if an error occurs
def load_balances(file_path):

    try:
        with open(file_path, "r") as file:
            entries = json.load(file)
        return entries
    except FileNotFoundError:
        print("File not found. Please check if debt_balances.json file exists")
        return[]
    except Exception as e:
        print(f"Unexpected error occured: {e}")
        return[]


# View a summary of all balances (if balance names are the same, add all entry amounts)

def balance_summaries(entries):
    # Initialize empty dictionary to contain summary of each balance
    total_balance = {}
    # For each entry in the JSON file, access the "Balance Name" & "Entry" values and store them into the variables: balance_name & entry_amount
    for entry in entries: 
        balance_name = entry["Balance Name"]
        entry_amount = entry["Entry"]
        # If a balance_name (e.g. Alice) is already in the total_balance dictionary, add its corresponding entry_amount to the existing entry total
        if balance_name in total_balance:
            total_balance[balance_name] += entry_amount
        # Else, if the balance_name is not yet a key in the total_balance dictionary, create a new key-value pair and set the value to the corresponding entry_amount
        else:
            total_balance[balance_name] = entry_amount
    # .items() method to iterate through total_balance dictionary and assign each balance_name with its corresponding total. Then print.
    for balance_name, total in total_balance.items():
        print(f"{balance_name}: ${total:.2f}")


# Create a balance (if balance name does not exist, create 1st entry (incl. balance name, entry amount & date))

# Delete a balance (if balance name = "x", delete entry)