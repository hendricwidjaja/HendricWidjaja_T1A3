from datetime import datetime
from file_operations import save_balance


FILE_PATH = "../data/debt_balances.json"

# Create a dictionary which contains all balance names with corresponding total debt amount
def calculate_total_balance(entries):
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
    return total_balance

# View a summary of all balances (if balance names are the same, add all entry amounts)
def balance_summaries(entries):
    # If "entries" is empty, advise the user that there are no balances available and execute "Create balance" function
    if not entries:
        print("No balances available. Create a new balance")
        create_balance(entries)
        print("---------------------------------")
        print("Debt Tracker 🎯")
        print("---------------------------------")
    # Initialize empty dictionary to contain summary of each balance
    total_balance = calculate_total_balance(entries)
    # .items() method to iterate through total_balance dictionary and assign each balance_name with its corresponding total. Then print.
    for balance_name, total in total_balance.items():
        print(f"{balance_name}: ${total:.2f}")

# Requests input from the user in the form of a date (YYYY-MM-DD).
# If user input is empty, returns today's date
# Date validation for error handling (checking if date entered is in YYYY-MM-DD format)    
def request_date(date_input):
    while True:
        user_date = input(date_input)
        if not user_date:
            return datetime.today().strftime("%Y-%m-%d")
        try: 
            datetime.strptime(user_date, "%Y-%m-%d")
            return user_date
        except ValueError:
            print("Date could not be recognised. Please enter a date using (YYYY-MM-DD) format.")

# Create a balance (if balance name does not exist, create 1st entry (incl. balance name, entry amount & date))
def create_balance(entries):

    print("Please enter the following details")
    balance_name = input("Balance Name: ")
    if any(entry["Balance Name"] == balance_name for entry in entries):
        print(f"'{balance_name}' already exists. Please create a balance with a unique name.")
        return 
    try:
        balance_amount = float(input("Balance Amount: "))
        if balance_amount < 0:
            print("Invalid entry amount. Balance cannot be less than $0")
            return
    except ValueError:
        print("Invalid entry. Amount can only include numbers")
        return
    
    print("-----------------------------------------------------------")
    print("NOTE: Leaving the date input blank will return today's date")
    balance_date = request_date("Date (YYYY-MM-DD): ")

    # Store new entry in "new_balance" variable
    new_balance = {"Balance Name": balance_name, "Entry": balance_amount, "Date": balance_date}
    # Append "new_balance" to entries
    entries.append(new_balance)
    # Use save_balance function to rewrite entries (incl. new_balance)
    save_balance(FILE_PATH, entries)
    print(f"Success! You have created a balance of ${balance_amount} for '{balance_name}'.")


# Delete a balance (if balance name = "x", delete entry)

# Select a balance (Allow user to view balance history)