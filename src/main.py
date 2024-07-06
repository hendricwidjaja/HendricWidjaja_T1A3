# Main program

#Import functions from operation files
from balance_operations import balance_summaries, create_balance, delete_balance, edit_balance, debt_calculator
from file_operations import load_balance, save_balance

# Determine file path
FILE_PATH = "../data/debt_balances.json"

# Main program showing options
def main ():
    # Use load_balances function to read/load balance entries and store into "entries" variable
    entries = load_balance(FILE_PATH)
    
    while True:
        print("---------------------------------")
        print("Debt Tracker 🎯")
        print("---------------------------------")

        balance_summaries(entries)

        print("---------------------------------")

        print("1. Create a new balance")
        print("2. Delete an existing balance")
        print("3. Edit/View a balance")
        print("4. Debt Calculator")        
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            create_balance(entries)
        elif choice == "2":
            entries = delete_balance(entries, "Balance Name")
        elif choice == "3":
            edit_balance(entries, "Balance Name")
        elif choice == "4":
            debt_calculator(entries, "Balance Name")
        elif choice == "5":
            save_balance(FILE_PATH, entries)
            print("All balance information has been saved. Thanks for using Debt Tracker 🎯. Come back soon!")
            break
        else:
            print("Please choose a valid option (1-5)")


if __name__ == "__main__":
    main()