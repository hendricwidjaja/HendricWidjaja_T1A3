from datetime import datetime, timedelta
import math
from colorama import Fore, Style
from emoji import emojize
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
        print(f"{Fore.RED}{emojize(':crying_face:')}  No balances available. Create a new balance{Fore.RESET}")
        create_balance(entries)
        print("---------------------------------")
        print(f"{Fore.BLUE}Debt Tracker 🎯{Fore.RESET}")
        print("---------------------------------")
    # Initialize empty dictionary to contain summary of each balance
    total_balance = calculate_total_balance(entries)
    # .items() method to iterate through total_balance dictionary and assign each balance_name with its corresponding total. Then print.
    for balance_name, total in total_balance.items():
        print(f"{emojize(':dollar_banknote:')} {Style.BRIGHT}{balance_name}:{Style.RESET_ALL} ${total:.2f}")

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
            print(f"{Fore.RED}{emojize(':crying_face:')} Date could not be recognised. Please enter a date using (YYYY-MM-DD) format.{Fore.RESET}")

# Create a balance (if balance name does not exist, create 1st entry (incl. balance name, entry amount & date))
def create_balance(entries):

    print(f"{Fore.BLUE}Please enter the following details: {Fore.RESET}")
    balance_name = input(f"{Fore.YELLOW}Balance Name: {Fore.RESET}")
    if any(entry["Balance Name"] == balance_name for entry in entries):
        print(f"{Fore.RED}{emojize(':crying_face:')} '{balance_name}' already exists. Please create a balance with a unique name.{Fore.RESET}")
        return 
    try:
        balance_amount = float(input(f"{Fore.YELLOW}Balance Amount: {Fore.RESET}"))
        if balance_amount < 0:
            print(f"{Fore.RED}{emojize(':crying_face:')} Invalid entry amount. Balance cannot be less than $0.{Fore.RESET}")
            return
    except ValueError:
        print(f"{Fore.RED}{emojize(':crying_face:')} Invalid entry. Amount can only include numbers.{Fore.RESET}")
        return
    
    print("-----------------------------------------------------------")
    print(f"{Style.BRIGHT}NOTE: Leaving the date input blank will return today's date.{Style.RESET_ALL}")
    print("-----------------------------------------------------------")
    balance_date = request_date(f"{Fore.YELLOW}Date (YYYY-MM-DD): {Fore.RESET}")

    # Store new entry in "new_balance" variable
    new_balance = {"Balance Name": balance_name, "Entry": balance_amount, "Date": balance_date}
    # Append "new_balance" to entries
    entries.append(new_balance)
    # Use save_balance function to rewrite entries (incl. new_balance)
    save_balance(FILE_PATH, entries)
    print(f"{Fore.GREEN}{emojize(':party_popper:')} Success! You have created a balance of ${balance_amount} for '{balance_name}'.{Fore.RESET}")


# Delete a balance (if balance name = "x", delete entry)
def delete_balance(entries, key):

    deletion_name = input(f"{Fore.YELLOW}Which balance would you like to delete?: {Fore.RESET}")
    if not any(entry["Balance Name"] == deletion_name for entry in entries):
        print(f"{Fore.RED}{emojize(':crying_face:')} '{deletion_name}' does not exist, please enter an existing balance to delete.{Fore.RESET}")
        return entries

    confirmation = input(f"{Fore.YELLOW}Are you sure you want to delete '{deletion_name}'? (Enter Y or N): {Fore.RESET}")
    if confirmation.lower() == "y":
        new_entries = []
        for entry in entries:
            if entry.get(key) != deletion_name:
                new_entries.append(entry)

        save_balance(FILE_PATH, new_entries)
        print(f"{Fore.GREEN}{emojize(':party_popper:')} '{deletion_name}' has been deleted successfully.{Fore.RESET}")
        return new_entries
    elif confirmation.lower() == "n":
        print(f"{Fore.RED}{emojize(':crying_face:')} Balance deletion for '{deletion_name}' has been cancelled.{Fore.RESET}")
        return entries
    # TypeError
    else:
        print(f"{Fore.RED}{emojize(':crying_face:')} User input cannot be recognised. Please try again.{Fore.RESET}")
        return entries

def account_balance_entries(entries, account_name, balance_name):

    combined_entries = []

    for entry in entries:
        if entry.get(account_name) == balance_name:
            combined_entries.append(entry)

    return combined_entries


# Choice total = list of entries from specific balance
# Prints all entries 
def balance_history(choice_total, balance_name):
    print("---------------------------------")
    print(f"{Fore.BLUE}{balance_name}'s Balance History:{Fore.RESET}")
    for each in choice_total:
        entry_value = each.get("Entry")
        entry_date = each.get("Date")
        print(f"{Style.BRIGHT}{entry_date}:{Style.RESET_ALL} ${entry_value}")


# Allows user to create an entry for selected balance
def create_entry(entries, choice_total, balance_name):
    choice_total_balance = sum(entry['Entry'] for entry in choice_total)
    try:
        entry_amount = float(input(f"{Fore.YELLOW}Entry Amount: {Fore.RESET}"))

        if choice_total_balance + entry_amount < 0:
            print(f"{Fore.RED}{emojize(':crying_face:')} Invalid entry amount. The balance cannot be less than $0.{Fore.RESET}")
            return
    except ValueError:
        print(f"{Fore.RED}{emojize(':crying_face:')} Invalid entry. Amount can only include numbers.{Fore.RESET}")
        return

    print("-----------------------------------------------------------")
    print(f"{Style.BRIGHT}NOTE: Leaving the date input blank will return today's date.{Style.RESET_ALL}")
    print("-----------------------------------------------------------")
    entry_date = request_date(f"{Fore.YELLOW}Date (YYYY-MM-DD): {Fore.RESET}")

    new_entry = {"Balance Name": balance_name, "Entry": entry_amount, "Date": entry_date}

    entries.append(new_entry)

    save_balance(FILE_PATH, entries)
    print(f"{Fore.GREEN}{emojize(':party_popper:')} Success! An entry of ${entry_amount} was created for '{balance_name}'{Fore.RESET}")
    return


# Allows user to delete an entry for selected balance
def delete_entry(entries, choice_total, balance_name):
    print(f"{Fore.BLUE}Balance History:{Fore.RESET}")
    for index, entry in enumerate(choice_total):
        print(f"{Fore.CYAN}{index + 1}{Fore.RESET}: {entry['Date']}: {entry['Entry']} ({balance_name})")
    try:
        entry_index = int(input(f"{Fore.YELLOW}Enter the index of the entry you want to delete: {Fore.RESET}")) - 1
        if 0 <= entry_index < len(choice_total):
            entry_to_delete = choice_total[entry_index]              
            entries.remove(entry_to_delete)
            save_balance(FILE_PATH, entries)
            print(f"{Fore.GREEN}{emojize(':party_popper:')} Entry {entry_index + 1} for '{balance_name}' has been deleted successfully!{Fore.RESET}")
        else:
            print(f"{Fore.RED}{emojize(':crying_face:')} Invalid input, please enter an index between 1 and {len(choice_total)}.{Fore.RESET}")
    except ValueError:
        print(f"{Fore.RED}{emojize(':crying_face:')} Value Error: Invalid input, please enter a valid index between 1 and {len(choice_total)}.{Fore.RESET}")


# Select a balance (Allow user to view balance history and edit balances)
def edit_balance(entries, key):
    print("---------------------------------")
    balance_name = input(f"{Fore.YELLOW}Which balance would you like to select? (Enter a balance name): {Fore.RESET}")
    choice_total = account_balance_entries(entries, key, balance_name)

    if not choice_total:
        print(f"{Fore.RED}{emojize(':crying_face:')} '{balance_name}' does not exist, please select an existing balance.{Fore.RESET}")
        return

    while True:
        balance_history(choice_total, balance_name)
        print("---------------------------------")
        print(f"{Fore.BLUE}What would you like to do?{Fore.RESET}")
        print(f"1. {emojize(':check_mark_button:')} Create an entry (increase or decrease)")
        print(f"2. {emojize(':cross_mark:')} Delete an entry")
        print(f"3. {emojize(':backhand_index_pointing_left:')} Back to main menu")
        print("---------------------------------")
        choice = input(f"{Fore.YELLOW}{emojize(':backhand_index_pointing_right:')} Choose an option: {Fore.RESET}")


        if choice == "1":
            create_entry(entries, choice_total, balance_name)
            choice_total = account_balance_entries(entries, key, balance_name)
        elif choice == "2":
            delete_entry(entries, choice_total, balance_name)
            choice_total = account_balance_entries(entries, key, balance_name)
        elif choice == "3":
            break
        else:
            print(f"{Fore.RED}{emojize(':crying_face:')} Invalid option, please try again (Enter 1 - 3).{Fore.RESET}")
            continue


# Calculates amount required for each recurring payment frequency to pay debt by certain date
def calculate_amount(entries, key, balance_name):
    # Get payment frequency from user + calculate time period by taking away first payment date from last payment date (in days)
    last_payment = request_date(f"{Fore.YELLOW}What date should the debt be paid in full? (YYYY-MM-DD): {Fore.RESET}")            
    frequency_choice = input(f"{Fore.YELLOW}How often will payments be made?: {Fore.RESET}" ).lower()

    frequency_selection = {
        "daily": 1,
        "weekly": 7,
        "fortnightly": 14,
        "monthly": (365/12)
        }

    if frequency_choice not in frequency_selection:
        print(f"{Fore.RED}{emojize(':crying_face:')} Invalid frequency choice, Please enter daily, weekly, fortnightly or monthly.{Fore.RESET}")
        return
    
    payment_period = frequency_selection[frequency_choice]

    first_payment = request_date(f"{Fore.YELLOW}What is the date of the first payment? (YYYY-MM-DD): {Fore.RESET}")

    try:
        last_payment_date = datetime.strptime(last_payment, "%Y-%m-%d").date()
        first_payment_date = datetime.strptime(first_payment, "%Y-%m-%d").date()
    except ValueError as e:
        print(f"{Fore.RED}{emojize(':crying_face:')} Dates could not be recognised: {e}{Fore.RESET}")
        return

    time_period = (last_payment_date - first_payment_date).days
    if time_period <= 0:
        print(f"{Fore.RED}{emojize(':crying_face:')} Error, the date of the first payment must be before the due date.{Fore.RESET}")
        return
    
    # Divide total days by payment frequency + calculate rounded down payment intervals
    payment_interval = time_period / payment_period
    adjusted_payment_interval = math.floor(payment_interval)

    # Calculate the payment amount required for each payment interval
    choice_total = sum(entry["Entry"] for entry in account_balance_entries(entries, key, balance_name))
    payment_amount = choice_total / payment_interval
    payment_amount_rounded = round(payment_amount, 2)

    # Calculate final payment required for when payment intervals have remainder days that don't fit in time period.
    final_payment = choice_total - (payment_amount_rounded * adjusted_payment_interval)

    # Print statement to user
    print(f"{Fore.GREEN}{emojize(':party_popper:')} To pay off '{balance_name}'s debt by {last_payment}, you'll need to pay ${payment_amount_rounded} on a {frequency_choice} basis and ${final_payment:.2f} as a final payment.{Fore.RESET}")


# Calculate the date that debt will be paid off based off a recurring payment amount and frequency
def calculate_date(entries, key, balance_name):

    # Get payment period/frequency input from user
    frequency_choice = input(f"{Fore.YELLOW}How often will payments be made?: {Fore.RESET}" ).lower()

    frequency_selection = {
        "daily": 1,
        "weekly": 7,
        "fortnightly": 14,
        "monthly": (365/12)
        }
    
    if frequency_choice not in frequency_selection:
        print(f"{Fore.RED}{emojize(':crying_face:')} Invalid frequency choice, Please enter daily, weekly, fortnightly or monthly.{Fore.RESET}")
        return
    
    payment_period = frequency_selection[frequency_choice]

    # Get $ amount from user (incl. error handling to ensure amount is greater than $0)
    try:
        payment_amount = float(input(f"{Fore.YELLOW}How much can be paid {frequency_choice}?: {Fore.RESET}"))
        if payment_amount <= 0:
            print(f"{Fore.RED}{emojize(':crying_face:')} Payment amount must be greater than $0.{Fore.RESET}")
            return
    except ValueError:
        print(f"{Fore.RED}{emojize(':crying_face:')} Error, amount could not be detected. Please enter a valid amount.{Fore.RESET}")
        return

    # Get date of first payment from user & convert into date format
    first_payment = request_date(f"{Fore.YELLOW}What is the date of the first payment? (YYYY-MM-DD): {Fore.RESET}")
    first_payment_date = datetime.strptime(first_payment, "%Y-%m-%d").date()

    # Retrieve total balance information of chosen account
    choice_total = sum(entry["Entry"] for entry in account_balance_entries(entries, key, balance_name))
    
    # Calculate days required to pay off debt using total balance, payment period and payment amount
    days_required = (choice_total / payment_amount) * payment_period

    # Calculate final date for when debt will be paid (in date format)
    final_debt_payment = first_payment_date + timedelta(days=days_required)

    # Convert date format of 'final debt payment' to a string
    final_debt_payment_date = final_debt_payment.strftime("%Y-%m-%d")

    # Print results to user
    print(f"{Fore.GREEN}{emojize(':party_popper:')} If ${payment_amount:.2f} is paid on a {frequency_choice.lower()} basis starting on {first_payment}, the debt for '{balance_name}' will be paid off by {final_debt_payment_date}.{Fore.RESET}")


# Allows user to calculate debt based off 2x options.
# Option 1: Allow user to calculate payment amount required to pay off specific debt by a certain date based off recurring payment frequency
# Option 2: Allow user to calculate date that a specific debt will be paid off based off recurring payment amount & frequency
def debt_calculator(entries, key):
    balance_name = input(f"{Fore.YELLOW}Which balance would you like to select? (Enter a balance name): {Fore.RESET}")
    choice_total = account_balance_entries(entries, key, balance_name)

    if not choice_total:
        print(f"{Fore.RED}{emojize(':crying_face:')} '{balance_name}' does not exist, please select an existing balance.{Fore.RESET}")
        return

    while True:
        print("---------------------------------")
        balance_summaries(choice_total)
        print("---------------------------------")
        print(f"{Fore.YELLOW}Frequency options = time period (daily, weekly, fortnightly, monthly){Fore.RESET}")
        print("---------------------------------")
        print(f"{Fore.BLUE}What would you like to calculate?{Fore.RESET}")
        print(f"1. {emojize(':money_bag:')} Calculate the payment amount required to pay off '{balance_name}' by a certain date, based off a recurring payment frequency.")
        print(f"2. {emojize(':tear-off_calendar:')} Calculate the date that '{balance_name}' will be paid off based off a recurring payment amount & frequency.")
        print(f"3. {emojize(':backhand_index_pointing_left:')} Back to main menu")
        print("---------------------------------")
        choice = input(f"{Fore.YELLOW}{emojize(':backhand_index_pointing_right:')} Choose an option: {Fore.RESET}")
        if choice == "1":
            calculate_amount(entries, key, balance_name)
        elif choice == "2":
            calculate_date(entries, key, balance_name)
        elif choice == "3":
            return
        else:
            print(f"{Fore.RED}{emojize(':crying_face:')} Please choose a valid option (1-3).{Fore.RESET}")