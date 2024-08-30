# Word Guessing Game

This Python script is a simple word-guessing game where the player has to guess a randomly chosen word, one letter at a time. The player has six chances to guess the word, and they can ask for a clue if needed.

## Features

- Randomly selects a word from a predefined list.
- Provides a hint with the first and last letter of the word if requested.
- Tracks the number of correct guesses.
- Allows the player to guess the entire word at the end.

## Prerequisites

- Python 3.x installed on your system.

## How to Play

1. **Start the Game:**
   - Run the script by executing the following command in your terminal or command prompt:
     ```bash
     python word_game.py
     ```
   - Replace `word_game.py` with the actual name of your Python file.

2. **Enter Your Name:**
   - The game will prompt you to enter your name. This will personalize your gaming experience.

3. **Guess the Letters:**
   - You will have 6 chances to guess the letters in the word.
   - If you guess a correct letter, it will be added to your list of correct guesses.
   - After 4 incorrect guesses, you will be given the option to receive a hint, which reveals the first and last letter of the word.

4. **Guess the Whole Word:**
   - At the end of the 6 chances, you will be asked to guess the entire word.
   - If you guess correctly, you win! If not, the game will inform you that you've lost.

## Important Notes

- The game uses a predefined list of words: `['hello','dog','apple','class','orange','melon','straw','game','word','elephant','good','marvel','disney']`.
- The hint reveals the first and last letter of the chosen word.
- The game ends after 6 chances, regardless of how many correct letters you have guessed.

## Example Output

Enter your name: John
Welcome to word game John
You will have 6 chances to guess the word
guess a letter: a
Incorrect guess
guess a letter: e
you have guessed one letter correctly
...

Lets see how much you have guessed the word: 
You have guessed 2 letters correctly and the letters are: ['e', 'l']

Now guess the whole word
Enter the whole word: apple
Congratulations You got it !!!!

## License

This script is free to use and modify for personal or educational purposes.
