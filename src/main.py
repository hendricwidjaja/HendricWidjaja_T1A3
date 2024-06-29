# Main program

#Import functions from operation files
from balance_operations import load_balances, balance_summaries, save_balance, create_balance

# Determine file path
FILE_PATH = "../data/debt_balances.json"

# Main program showing options
def main ():
    # Use load_balances function to read/load balance entries and store into "entries" variable
    entries = load_balances(FILE_PATH)
    # If "entries" is empty, advise the user that there are no balances available and execute "Create balance" function
    if not entries:
        print("Debt Tracker 🎯")
        print("------------------")
        print("No balances available. Create a new balance")
        # Insert function to create a balance
    
    while True:
        print("Debt Tracker 🎯")
        print("------------------")

        balance_summaries(entries)

        print("------------------")

        print("1. Create a new balance")
        print("2. Delete an existing balance")
        print("3. Select a balance")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            create_balance(entries)
        elif choice == "2":
            print("Delete balance functionality to be implemented")
        elif choice == "3":
            print("Select a balance functionality to be implemented")
        elif choice == "4":
            print("Thanks for using Debt Tracker 🎯. Come back soon!")
            break
        else:
            print("Please choose a valid option (1-4)")


if __name__ == "__main__":
    main()