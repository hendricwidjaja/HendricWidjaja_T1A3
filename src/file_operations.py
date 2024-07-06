import json
from colorama import Fore
from emoji import emojize


FILE_PATH = "../data/debt_balances.json"


def load_balance(file_path):
# Load balances from JSON file to access entries
    try:
        with open(file_path, "r") as file:
            entries = json.load(file)
        return entries
    except FileNotFoundError:
        print(f"{Fore.RED}{emojize(':crying_face:')} File not found. Please check if debt_balances.json file exists.{Fore.RESET}")
        return[]
    except json.JSONDecodeError:
        print(f"{Fore.RED}{emojize(':crying_face:')} Decoding error detected in balance database (JSON file): {e}{Fore.RESET}")
        return []
    except Exception as e:
        print(f"{Fore.RED}{emojize(':crying_face:')} Unexpected error occured: {e}{Fore.RESET}")
        return[]


def save_balance(file_path, entries):
# Save a new balance/entry into the JSON file
    try:
        with open(file_path, "w") as file:
            json.dump(entries, file, indent=4)
    except Exception as e:
        print(f"{Fore.RED}{emojize(':crying_face:')} Error. Entry failed to save: {e}{Fore.RESET}")