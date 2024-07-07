from balance_operations import(
    balance_summaries, create_balance, debt_calculator, 
    delete_balance, edit_balance
)
from file_operations import load_balance, save_balance
from colorama import Fore, Style
from emoji import emojize


# Determine file path for balance data
FILE_PATH = "../data/debt_balances.json"


def main():
# Main function displaying main menu
    entries = load_balance(FILE_PATH)
    
    while True:
        print("---------------------------------")
        print(f"{Fore.BLUE}Debt Tracker {emojize(':bullseye:')}{Fore.RESET}")
        print("---------------------------------")
        balance_summaries(entries)
        print("---------------------------------")
        print(f"1. {emojize(':check_mark_button:')} Create a new balance")
        print(f"2. {emojize(':cross_mark:')} Delete an existing balance")
        print(f"3. {emojize(':eyes:')} Edit/View a balance")
        print(f"4. {emojize(':robot:')} Debt Calculator")        
        print(f"5. {emojize(':waving_hand:')} Exit")

        choice = input(f"{Fore.YELLOW}{emojize(':backhand_index_pointing_right:')} Choose an option: {Fore.RESET}")

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
            print(f"{Style.BRIGHT}All balance information has been saved. Thanks for using Debt Tracker 🎯. Come back soon!{Style.RESET_ALL}")
            break
        else:
            print(f"{Fore.RED}{emojize(':crying_face:')} Please choose a valid option (1-5){Fore.RESET}")


if __name__ == "__main__":
    main()