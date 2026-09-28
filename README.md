How to Run the Project

Follow the steps below to run the Smart Banking System on your computer.

1. Install Python

This project is written completely in Python, so Python must be installed on your computer.

You can check whether Python is already installed by opening Command Prompt, PowerShell, or the VS Code Terminal and running:

python --version

If Python is installed correctly, you will see something similar to:

Python 3

If the command does not work, install Python and make sure the "Add Python to PATH" option is enabled during installation.

2. Download the Project

Download this project from GitHub using the Code → Download ZIP option.

After downloading:

Go to your Downloads folder.
Find the downloaded ZIP file.
Extract the ZIP file.
Open the extracted Smart_Banking_System folder.

3. Open the Project in VS Code

Open Visual Studio Code.

Then select:

File → Open Folder

Choose the Smart_Banking_System folder.

Make sure you open the project folder itself, not just one of the Python files.

4. Check the Python Files

Before running the program, make sure all the .py files are present in the same folder.

The project uses multiple Python files, so deleting or moving one of them may cause an import error.

For example:

main.py
account.py
account_manager.py
banking.py
transactions.py
rewards.py
calculator.py

should all be inside the same project folder.

5. Open the Terminal in VS Code

In VS Code, go to:

Terminal → New Terminal

A terminal will open at the bottom of the VS Code window.

You should see the project folder location in the terminal.

For example:

PS C:\Users\YourName\Desktop\Smart_Banking_System>
6. Run the Main Program

The main file of the project is main.py.

Run it using:

```bash
python main.py
```

Then press Enter.

If the python command does not work on Windows, try:

py main.py
7. Main Menu

After successfully running the program, the Smart Banking System will display the main menu in the terminal.

From there, you can create an account or log in to an existing account.

The program will guide you through the available options.

8. Creating an Account

If you are using the program for the first time:

Select the Create Account option.
Enter your name.
Create a password.
The program will generate an account number.
Keep the account number and password for logging in.

Example:

Enter your name: Rahul
Create password: 1234

Account created successfully!
Your Account Number: SB123456
9. Logging In

After creating an account, select the Login option.

Enter:

Account number
Password

The program allows a limited number of login attempts for security.

After successful login, the banking menu will be displayed.

10. Using Banking Features

After logging in, you can select different operations from the banking menu.

For example:

Check Balance

Displays the current account balance.

Deposit Money

Allows you to add money to the account.

Withdraw Money

Allows you to withdraw money if sufficient balance is available.

Transfer Money

Allows you to transfer money to another account within the program.

Transaction History

Displays previous transactions.

Account Details

Shows the basic information related to the account.

Reward Points

Displays the reward points earned through transactions.

Interest Calculator

Allows you to calculate simple interest.

11. Exiting the Program

When you are finished using the banking system, select the Exit option from the menu.

The program will close and return you to the terminal.

Troubleshooting
python is not recognized

If you get an error like:

'python' is not recognized as an internal or external command

try:

```bash
py main.py
```

If that also does not work, Python may not be installed correctly or may not have been added to PATH.

ModuleNotFoundError

If you get an error such as:

ModuleNotFoundError

check that all the project .py files are present in the same folder.

For example, if main.py imports banking.py, make sure banking.py has not been moved or renamed.

Program does not start

Make sure you are running the command from inside the project folder.

You can check the files in the current folder using:

dir

You should see:

main.py
account.py
account_manager.py
banking.py
transactions.py
rewards.py
calculator.py

Then run:
```bash
python main.py
```
