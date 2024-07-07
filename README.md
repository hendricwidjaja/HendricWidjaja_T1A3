# T1A3: Terminal Application (Debt Tracker 🎯)

Welcome to the documentation of Hendric Widjaja's - T1A3: Terminal Application.

# Quick Links

Please use the links below to quickly access key parts of this documentation

- [Link to source control repository (GitHub)](#source-control-repository)
- [Code Style Guide / Styling Conventions (PEP8)](#code-style-guide--styling-conventions-pep8)
- [Application Features](#application-features)
    - [Main Features](#main-features)
        - Create Balance
        - Delete Balance
        - Create Entry
        - Delete Entry
        - Calculate Amount
        - Calculate Date
    - [Other Features](#other-features)
- [Implementation Plan (Trello)](#implementation-plan-trello)
- [Help Documentation](#help-documentation)


## Source Control Repository
Please find the link to the source control repository for this application below:
[https://github.com/hendricwidjaja/HendricWidjaja_T1A3](https://github.com/hendricwidjaja/HendricWidjaja_T1A3)


## Code Style Guide / Styling Conventions (PEP8)
The [PEP8 Style Guide for Python Code](https://peps.python.org/pep-0008/#indentation) (written by Guido van Rossum, Barry Warsaw & Alyssa Coghlan) was implemented for the writing of this application's code. The review of this implementation was conducted manually and made to ensure that the following styling was allowed for:
- Imports to be located at the top of each file
- Imports to be grouped by standard, 3rd party and local application
- 4 spaces per indentation level
- 79 character maximum line limit (where applicable)
- 72 character maximum line limit for long blocks (where applicable)
- Consistency of hanging indent application for continuation lines
- Snake case with lower characters for all variable (e.g. snake_case)
- Upper case with underscores for all constants (e.g. UPPER_CASE)
- Consistency of 2x blank lines between functions
- Consistency of 1x blank where necessary to break up code blocks
- Consistency of double quotes for all strings (if possible)
- Ensure use of white-space characters are consistent and avoided:
    - immediately inside parentheses, brackets or braces
    - between trailing commas,
    - before commas, semicolon or colon
    - immediately before open parenthesis
- Descriptive variable names


## Application Features
There are several features within this application which can be broken down into the below categories. A brief description for each function has been provided for clarification, however the main features will be explained in greater depth.

<b>NOTE:</b> If any images of functions are difficult to see, please refer to the [main functions folder](./docs/main_functions/) within the zip file.

### Main Features

<i><b>NOTE:</b> No explanations will be provided for coloured text (Colorama) or emojis (Emoji). The implementation of these have been for the sole purpose of aesthetics and UX/UI design.</i>

<b>Main Features</b> (Core functions which require various inputs from the user to either update data files or provide a calculated output)
- Create Balance Function
    - This function allows the creation of an entirely new balance into the JSON file. It will require various user input such as “Balance Name”, “Balance amount” and “Date” of entry. It will ensure that the user input is inserted into the JSON file in the correct format. Please see detailed breakdown of function below with inline comments:

    ![Create Balance Function with comments](./docs/main_functions/create_balance_function.png)

- Delete Balance Function
    - This function is a main feature and will allow the user to delete a specific balance from the JSON file. As it cannot be undone, it will require a confirmation from user that they want to delete the specific balance. It will require user input to enter the balance name they want to delete and rewrite the JSON file with a new list which does not contain the specified balance name entries. Please see detailed breakdown of function below with inline comments:

    ![Delete Balance Function with comments](./docs/main_functions/delete_balance_function.png)


- Create Entry Function
    - This main feature allows the user to create a new entry for a specified balance. This is done by requesting inputs from the user such as “date” of entry and “entry amount”. The program will append this new entry into the JSON file and save/overwrite this as the new updated file. A message will then be printed to the user to advise if the entry was entered successfully. Please see detailed breakdown of function below with inline comments:

    ![Create Entry Function with comments](./docs/main_functions/create_entry_function.png)
    
- Delete Entry Function
    - The main feature allows the user to delete an entry from the JSON file for a pre-specified balance. The function firstly prints all the entries for the specified balance with its corresponding index (as well as “date” of entry and “entry amount”). It will then request an index number as an input from the user to be deleted. The corresponding entry of the index number will then be removed from the JSON file and the updated file will be saved/overwritten without the deleted entry. A message will then be printed to the user that the specific entry has been deleted. Please see detailed breakdown of function below with inline comments:

    ![Delete Entry Function with comments](./docs/main_functions/delete_entry_function.png)

- Calculate Amount Function
    - The function allows the user to calculate the payment amount required to pay off a debt by a certain date, based off a recurring payment frequency. This is done by requesting inputs from the user (recurring payment frequency and date of when the debt needs to be paid off). Further calculations (using basic algebra) are then completed by the script to output a payment amount. These calculations utilise datetime & math modules/functions. Please see detailed breakdown of function below with inline comments:

    ![Calculate Amount Function with comments](./docs/main_functions/calculate_amount_function.png)

- Calculate Date Function
    - The function allows the user to calculate the date that a debt will be paid off based off a recurring payment amount and frequency. This is done by requesting inputs from the user (recurring payment frequency and payment amount). Further calculations (using basic algebra) are then completed by the script to output a payment date. These calculations utilise datetime & math modules/functions. Please see detailed breakdown of function below with inline comments:

    ![Calculate Date Function with comments](./docs/main_functions/calculate_date_function.png)

### Other Features

<b><u>Main menus</u></b> (functions which display choices to the user that allow them to provide input to access different functions)
- Menu #1: Main Menu
    - Create a main menu for the user to allow them to navigate through the application providing opportunity for user input.
- Menu #2: Edit/View Balance Menu
    - Creates a menu for the user to edit and view a specific balance. The menu includes:
        - Creating an entry
        - Deleting an entry
        - Going back to main menu
    - Menu also prints a summary of specific balance to allow easier choice making for the user.
- Menu #3: Debt Calculator Menu
    - Debt calculator menu provides options for the user to calculate debt of specific balance with the below options:
        - Allow user to calculate the payment amount required to pay off a debt by a certain date, based off a recurring payment frequency
        - Allow user to calculate the date that a debt will be paid off based off a recurring payment amount and frequency
    - Menu also includes helpful text to identify the meaning of “frequency options”, etc.

<b><u>Sub-functions</u></b> (functions which have been modularised to allow for the implementation of DRY Coding Principles)
- Load Balance
    - This sub-function is not a main feature but is crucial to the functionality of many functions which involve access to the JSON file to view or edit entries.
- Save Balance
    - This sub-function is not a main feature but is crucial to the functionality of various other functions. This function will allow the overwriting of the JSON file with updated entries based of user choice of deletion or addition.
- Create Balance Summaries
    - This sub-function allows functionality of other functions within the program. It’s main purpose is to be modular so that it can be reused when the program requires to create a summary list of chosen balances.
- Calculate Total Balance
    - This sub-function has been modularised and forms as a function with the balance_summaries function. It allows for the extraction of “balance name” and “balance amounts” from the JSON file for all entries.
- Request Date
    - This function is used in various other functions to allow the program to request a date input form the user. It will handle all error handling for the date input ensuring it is in the correct format.
- Account Balance Entries
    - This sub-function is utilised in various other functions and is modularised to retrieve the specific entries in the JSON file which match the “balance name” specified by the user.
- Balance History
    - This sub-function has been modularised for the sole purpose of printing the entries for a specified balance which is chosen by the user. It will only print the “date” of the entries and the “entry amount” for a specific balance. This sub-function is only utilised to provide the user the information they require to select if they want to remove or create an entry for the specified balance (Edit/View menu).


## Implementation Plan (Trello)
Please find the link to the Trello board for this application below:
[https://trello.com/invite/b/XUAi4Y6a/ATTIc457de7463b016fe6016a00fdc8535abB3E00757/t1a3-terminal-application](https://trello.com/invite/b/XUAi4Y6a/ATTIc457de7463b016fe6016a00fdc8535abB3E00757/t1a3-terminal-application)

### Screenshots of each Trello card for the coding of this application are as per below
This includes:
- outlines of how each feature will be implemented and a checklist of tasks for each feature
- prioritise the implementation of different features or checklist items within a feature
- provide a deadline, duration or other time indicator for each feature or checklist-item

<b>NOTE:</b> If any images of functions are difficult to see, please refer to the [Trello folder](./docs/Trello/) within the zip file.


![Create/setup directories trello card](./docs/Trello/create_setup_directories.png)
![Setup remote repo/venv/gitignore trello card](./docs/Trello/setup_remote_repo.png)
![Create python files & JSON file trello card](./docs/Trello/create_python_files.png)
![Main menu trello card](./docs/Trello/main_menu.png)
![Edit/View Balance Menu trello card](./docs/Trello/edit_view_balance_menu.png)
![Debt Calculator menu trello card](./docs/Trello/debt_calculator_menu.png)
![Load Balance trello card](./docs/Trello/load_balance.png)
![Save Balance trello card](./docs/Trello/save_function.png)
![Create Balance Summaries trello card](./docs/Trello/create_balance_summaries.png)
![Create Balance Function trello card](./docs/Trello/create_balance_function_trello.png)
![Delete Balance Function trello card](./docs/Trello/delete_balance_function_trello.png)
![Calculate Total Balance trello card](./docs/Trello/calculate_total_balance.png)
![Request Date trello card](./docs/Trello/request_date.png)
![Account Balance Entries trello card](./docs/Trello/account_balance_entries.png)
![Balance History trello card](./docs/Trello/balance_history.png)
![Calculate Amount trello card](./docs/Trello/calculate_amount.png)
![Calculate Date trello card](./docs/Trello/calculate_date.png)
![Create Entry trello card](./docs/Trello/create_entry.png)
![Delete Entry trello card](./docs/Trello/delete_entry.png)
![Import Libraries trello card](./docs/Trello/import_libraries.png)
![Review Code Styling & Conventions trello card](./docs/Trello/review_code_style.png)
![Create Multiple Scripts trello card](./docs/Trello/create_multiple_scripts.png)
![DRY Coding principles review trello card](./docs/Trello/DRY_code.png)


## Help Documentation

### Important Notes
This documentation has been written for the purpose of providing information regarding:
- Steps to install the application
- Dependencies required by the application to operate
- Any system/hardware requirements
- How to use any command line arguments made for this application

The application comes with pre-populated data as per below. This can be deleted by either manually deleting the entries in the [debt_balances.json](./data/debt_balances.json) file or running the application and selecting option "2" on the main menu and following the prompts.

![Debt Tracker Main Menu screenshot](./docs/debt_tracker_main_menu.png)
- 

### Application Install Guide
The installation of Debt Tracker can be installed as per the below steps:

1. Download the 'HendricWidjaja_T1A3' zip file from the [GitHub](https://github.com/hendricwidjaja/HendricWidjaja_T1A3) repository for the application (if not done already).
2. Unzip the file
3. Right click the /src folder and select "New Terminal at folder".
4. Enter the command below to run the <u>main_script.sh</u> 
```
./main_script.sh
```
5. This script will run the application automatically including:
- checking for python3
- creating a virtual environment
- downloading required dependencies
- running the application
- deactivating the virtual environment once the application is closed

### Dependencies List
Python3 is required to run this app. If the below error appears when running the above steps, please go to [https://www.python.org/downloads/](https://www.python.org/downloads/) to download Python3.

```
You don't have Python3 installed. Please install Python3 and try again.
```

The required dependencies to run this application include:
- colorama==0.4.6
- emoji==2.12.1

<b>NOTE: If install is successful, the above dependencies will automatically be downloaded in the virtual environment.</b>

### System/Hardware Requirements
Python3 can be installed on a variety of operating systems. Please see below:

According to an [article](https://support.enthought.com/hc/en-us/articles/204273874-Enthought-Python-Minimum-Hardware-Requirements) by Jonathan March (25th January 2023), the below requirements would more than suffice. 
- Modern Operating System: 
    - Windows 7 or 10
    - Mac OS X 10.11 or higher, 64-bit
    - Linux: RHEL 6/7
- x86 64-bit CPU (Intel / AMD architecture). ARM CPUs are not supported.
- 4 GB RAM (preferred)
- 5 GB free disk space (preferred)

### Command Line Arguments
The Debt Tracker application has been designed to be user friendly and intuitive, with various tips on user input scattered throughout the application. The error handling messages that have been integrated allows the user to also re-attempt inputs correctly. A run through of how to execute the main functions of the application are listed below.

<b><i>NOTE: All steps start from the main menu of the application</i></b>

![Debt Tracker Main Menu](docs/debt_tracker_main_menu.png)

#### Create Balance Function
This function allows the creation of an entirely new balance into the JSON file. It will require various user input such as “Balance Name”, “Balance amount” and “Date” of entry. It will ensure that the user input is inserted into the JSON file in the correct format. Please follow the below steps:

1. Input "1" in the command line to execute "Create a new balance" option.
2. Input a name for the new balance (e.g. "Example 3")
3. Input an amount for the balance (e.g. "500")
4. Input a date in YYYY-MM-DD format (e.g. "2024-07-07)
    - <i>Note: If no input is inserted, the date will automatically be set to today's date.</i>
5. A success message will appear if you have completed the above steps correctly.

![Create balance function example](docs/create_balance_example.png)

#### Delete Balance Function
This function is a main feature and will allow the user to delete a specific balance from the JSON file. As it cannot be undone, it will require a confirmation from user that they want to delete the specific balance. It will require user input to enter the balance name they want to delete and rewrite the JSON file with a new list which does not contain the specified balance name entries. Please follow the below steps:

1. Input "2" in the command line to execute "Delete an existing balance" option.
2. Input the name of the balance you wish to delete (e.g. "Balance 3")
    - <i>NOTE: This input is case sensitive. An error message will appear if the user input does not match any balance names.</i>
3. Input "Y" or "N" when the program asks if you are sure you want to delete the balance.
4. A success message will appear if you have completed the above steps correctly.

![Delete Balance Function example](docs/delete_balance_example.png)

#### Create Entry Function
This main feature allows the user to create a new entry for a specified balance. This is done by requesting inputs from the user such as “date” of entry and “entry amount”. The program will append this new entry into the JSON file and save/overwrite this as the new updated file. A message will then be printed to the user to advise if the entry was entered successfully. Please follow the below steps:

1. Input "3" in the command line to execute "Edit/View a balance" option.
2. Input the name of the balance you would like to edit/view (e.g. "Example 2")
    - <i>NOTE: A balance history of the selected balance will appear and a new menu will appear.</i>
3. Input "1" in the command line to execute "Create an entry (increase or decrease)" option.
4. Input an "Entry Amount" (e.g. 250)
5. Input a date in YYYY-MM-DD format (e.g. "2024-07-07)
6. A success message will appear if you have completed the above steps correctly.
    - <i>NOTE: The program will take the user back to the 'edit/view' menu where the user will be able to see the newly created entry.</i>

![Create Entry Function Example](docs/create_entry_example.png)

    
#### Delete Entry Function
The main feature allows the user to delete an entry from the JSON file for a pre-specified balance. The function firstly prints all the entries for the specified balance with its corresponding index (as well as “date” of entry and “entry amount”). It will then request an index number as an input from the user to be deleted. The corresponding entry of the index number will then be removed from the JSON file and the updated file will be saved/overwritten without the deleted entry. A message will then be printed to the user that the specific entry has been deleted. Please follow the below steps:

1. Input "3" in the command line to execute "Edit/View a balance" option.
2. Input the name of the balance you would like to edit/view (e.g. "Example 2")
    - <i>NOTE: A balance history of the selected balance will appear and a new menu will appear.</i>
3. Input "2" in the command line to execute "Delete an entry" option.
    - <i>NOTE: An updated balance history will appear which now includes an index number in CYAN for each entry.</i>
4. Input the index number of the entry you want to delete (e.g. enter "2" to delete entry 2 that is listed on the balance history)
5. A success message will appear if you have completed the above steps correctly.
    - <i>NOTE: The program will take the user back to the 'edit/view' menu where the user will be able to see the updated balance entries.</i>

![Delete Entry Function Example](docs/delete_entry_example.png)

#### Calculate Amount Function
The function allows the user to calculate the payment amount required to pay off a debt by a certain date, based off a recurring payment frequency. This is done by requesting inputs from the user (recurring payment frequency and date of when the debt needs to be paid off). Further calculations (using basic algebra) are then completed by the script to output a payment amount. These calculations utilise datetime & math modules/functions. Please follow the below steps:

1. Input "4" in the command line to execute "Debt Calculator" option.
2. Input the name of the balance you would like to use the debt calculator options on (e.g. "Example 2").
    - <i>NOTE: A summary of the total balance amount for the selected balance will appear for the user's reference.</i>
3. Input "1" in the command line to execute "Calculate the payment amount required to pay off "Example 2" by a certain date, based off a recurring payment frequency" option.
    - <i>NOTE: If a different balance is selected, "Example 2" will be replaced by the selected balance's name.</i>
4. Input a date in YYYY-MM-DD format for when the debt should be paid in full (e.g. "2024-09-20")
5. Input a frequency option ('daily', 'weekly', 'fortnightly' or 'monthly') which payments can be made on a consistent basis (e.g. "daily").
6. Input a date in YYYY-MM-DD format for when the first payment will be made (e.g. "")
    - <i>NOTE: The example below demonstrates inserting a blank input, which automatically selects today's date.</i>
7. A success message will appear providing the results of the inputs, advising the user the amount that needs to be paid on a recurring payment frequency (and any additional finaly payment amount) in order for the debt to be paid by a certain date.

![Calculate Amount Function Example](docs/calculate_amount_example.png)

#### Calculate Date Function
The function allows the user to calculate the date that a debt will be paid off based off a recurring payment amount and frequency. This is done by requesting inputs from the user (recurring payment frequency and payment amount). Further calculations (using basic algebra) are then completed by the script to output a payment date. These calculations utilise datetime & math modules/functions. Please follow the below steps:

1. Input "4" in the command line to execute "Debt Calculator" option.
2. Input the name of the balance you would like to use the debt calculator options on (e.g. "Example 2").
    - <i>NOTE: A summary of the total balance amount for the selected balance will appear for the user's reference.</i>
3. Input "2" in the command line to execute "Calculate the date that 'Example 2' will be paid off based off a recurring payment amount & frequency" option.
    - <i>NOTE: If a different balance is selected, "Example 2" will be replaced by the selected balance's name.</i>
4. Input a frequency option ('daily', 'weekly', 'fortnightly' or 'monthly') which payments can be made on a consistent basis (e.g. "weekly").
5. Input an amount which can be paid per frequency option (e.g. "25")
    - <i>NOTE: The above step would imply that $25 will be paid on a weekly basis.</i>
6. Input a date in YYYY-MM-DD format for when the first payment will be made (e.g. "2024-08-01")
7. A success message will appear providing the results of the inputs, advising that if the user pays $x amount on the chosen frequency period, the selected debt will be paid by a certain date.

![Calculate Date Function Example](docs/calculate_date_example.png)