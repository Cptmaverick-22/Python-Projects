| Build | Tests | Coverage |
| :---: | :----: | :------: | 
| [![Build Status](badge)]([link](https://img.shields.io/badge/any_text-you_like-blue)) | [![Tests](badge)](link)| [![Coverage](badge)](link) |

# Random Dice Roller

This Python script simulates rolling a six-sided die multiple times. The user can choose how many times they want to roll the die, and after each set of rolls, they are asked if they want to roll again.

## Features

- Simulates rolling a six-sided die.
- Allows the user to specify how many times they want to roll the die in each round.
- Prompts the user to roll again or exit after each round.

## Prerequisites

- Python 3.x installed on your system.

## How to Use

1. **Run the Script:**
   - Execute the script using the following command in your terminal or command prompt:
     ```bash
     python dice_roller.py
     ```
   - Replace `dice_roller.py` with the actual name of your Python file.

2. **Input the Number of Rolls:**
   - When prompted, enter the number of times you want to roll the die in the current round.

3. **View the Results:**
   - The script will display the result of each roll.

4. **Roll Again or Exit:**
   - After each round, you will be asked if you want to roll again.
   - Type `yes` to roll again or `no` to exit the program.

## Example Output

```
Random Dice Roller
Enter the times you want to roll: 3
Rolling dice 1 time giving point: 4
Rolling dice 2 time giving point: 2
Rolling dice 3 time giving point: 6

want to roll again? (yes/no): yes
Enter the times you want to roll: 2
Rolling dice 1 time giving point: 5
Rolling dice 2 time giving point: 3

want to roll again? (yes/no): no
Thank you for playing

```


## Important Notes

- The script uses Python's `random` module to generate random numbers between 1 and 6, simulating a six-sided die.
- The script will continue to prompt the user to roll again until they choose to exit.

## License

This script is free to use and modify for personal or educational purposes.
