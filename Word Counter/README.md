# Word Count Script

This Python script counts the number of words in a text file.

## Features

- Opens a specified text file
- Reads the contents of the file
- Splits the content into words
- Prints the total number of words in the file

## Prerequisites

- Python 3.x installed on your system

## How to Use

1. **Place the Text File:**
   - Ensure that the text file you want to count words in is named `Convert to txt.txt`.
   - Place the file in the same directory as the Python script.

2. **Run the Script:**
   - Open a terminal or command prompt.
   - Navigate to the directory where the script is located.
   - Run the following command:
     ```bash
     python word_count.py
     ```
   - Replace `word_count.py` with the name of your Python file if different.

3. **View the Output:**
   - The script will output the total number of words in the text file.

## Important Notes

- The script assumes that the file `Convert to txt.txt` is present in the same directory as the Python script.
- If the file is named differently or located elsewhere, modify the script accordingly to point to the correct file.

## Troubleshooting

- **FileNotFoundError:** If you receive this error, ensure that the `Convert to txt.txt` file exists in the same directory as the script.
- **Empty File:** If the text file is empty, the script will output `0` as the word count.

## License

This script is free to use and modify for personal or educational purposes.
