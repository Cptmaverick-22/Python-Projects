# Word Guessing Game

Welcome to the Word Guessing Game! This is a simple command-line game where you have to guess a word by predicting its letters. You will have 6 chances to guess the word correctly. If you're confident, you can attempt to guess the entire word before your chances run out. Good luck!

## Features

- Guess a random word from a predefined list of words.
- You have 6 chances to guess the letters of the word.
- You can request a clue after 3 incorrect guesses, which will reveal the first and last letters of the word, along with its length.
- You can also choose to guess the entire word at any point by typing `quit`.
- The game will congratulate you if you guess the word correctly or reveal the correct word if you don't.

## How to Play

1. Run the script.
2. Enter your name.
3. You will be greeted and informed of the rules.
4. Start guessing letters one by one.
5. After 3 guesses, you can request a clue.
6. If you feel confident, you can type `quit` to guess the entire word.
7. At the end of 6 chances, guess the whole word.
8. The game will tell you if you guessed correctly or not.

## Prerequisites

- Python 3.x
- The `random` module (standard with Python)

## How to Run the Game

1. Clone this repository or download the script.
2. Run the script using Python:

   ```
   python word_guessing_game.py
   ```

## Example gameplay

```
Enter your name: John

Welcome to word game John

You will have 6 chances to guess the word

guess a letter or type 'quit' to guess the complete word: h
You have guessed one letter correctly! 'h' appears 1 Time

guess a letter or type 'quit' to guess the complete word: a
Incorrect guess

guess a letter or type 'quit' to guess the complete word: t
Incorrect guess

will you want to have a clue: yes
The first and last letter of the word is: h e
The length of the word is: 5

guess a letter or type 'quit' to guess the complete word: quit
Enter the whole word: horse
Ahh, you lose :(  The correct word was: hello

Please press enter to leave the program

```

## License

This project is licensed under the GPL License - see the LICENSE file for details.
