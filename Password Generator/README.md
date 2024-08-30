# Password Generator

This Python script generates a random password based on the user's desired difficulty level. The user can choose between three difficulty levels: Easy, Medium, and Hard.

## Features

- **Easy:** Generates a password containing one uppercase letter, and the rest are lowercase letters and digits.
- **Medium:** Generates a password containing one special character, with the rest being a mix of uppercase, lowercase, and digits.
- **Hard:** Generates a password that includes uppercase letters, lowercase letters, digits, and special characters.

## Prerequisites

- Python 3.x installed on your system.

## How to Use

1. **Run the Script:**
   - Execute the script using the following command in your terminal or command prompt:
     ```bash
     python password_generator.py
     ```
   - Replace `password_generator.py` with the actual name of your Python file.

2. **Input the Length:**
   - You will be prompted to enter the desired length of your password.

3. **Choose Difficulty:**
   - The script will ask you to select a difficulty level: EASY, MEDIUM, or HARD.
   - Based on your choice, the password will be generated with the corresponding complexity.

4. **View the Generated Password:**
   - The generated password will be displayed on the screen.

## Example Output

- Password generator:
- Enter the length of the password you want: 12
- Enter the difficulty of your password (EASY) (MEDIUM) (HARD): hard
- The generated password is: 7E#mJ2qaS!eX

## Important Notes

- The script uses Python's `random` and `string` libraries to generate the password.
- Special characters used in the `MEDIUM` and `HARD` levels are from the following set: `!@#$%^&*<>,.-+?_`.

## License

This script is free to use and modify for personal or educational purposes.
