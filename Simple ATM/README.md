
# ATM Machine - Python Project

## Overview

This is a simple Python-based ATM machine simulation that allows users to:
- Deposit money
- Withdraw money
- Check their balance

The system requires the user to enter their name and PIN to authenticate. It also ensures that the user cannot withdraw more than their available balance. The user can exit the system at any time by pressing 'q'.

## Features

- **Authentication:** The user must provide a name and correct PIN to access their account.
- **Deposit:** Users can deposit any amount of money into their account.
- **Withdraw:** Users can withdraw money if they have sufficient balance.
- **Check Balance:** Users can view their current account balance.
- **Exit:** Users can exit the ATM interface anytime by pressing 'q'.

## Installation

1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/yourusername/atm-machine.git
    ```
2. Ensure you have Python installed on your machine (version 3.x).

## How to Run

1. Open a terminal or command prompt in the directory where the script is located.
2. Run the script using Python:
    ```bash
    python atm_machine.py
    ```

## Example Usage

Upon running the program, you will be prompted to enter your details (name, PIN, and balance). After that, you will be asked if you'd like to use the ATM. Once inside, you can deposit, withdraw, check your balance, or exit.

```
Enter Your Name: John
Enter Your PIN: 1234
Enter the Balance: 1000
Do you want to use ATM? yes

Enter Your Name: John
Enter your PIN: 1234
Press 1 for deposit 
2 for withdraw 
3 for checking balance

Enter your choice or press 'q' to exit: 1
Enter the amount you want to deposit: 500

Enter your choice or press 'q' to exit: 3
Available Balance: 1500
```

## LICENSE
This project is licensed under the GPL License - see the LICENSE file for details.


