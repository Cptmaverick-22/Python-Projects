import random as rn

words = ['hello','dog','apple','class','orange','melon','straw','game','word','elephant','good','marvel','disney']
random_choice = rn.choice(words)
hint = random_choice[0]+random_choice[-1]

name = input("Enter your name: ")
print("Welcome to word game",name)
print("You will have 6 chances to guess the word")
chance = 6
guessed = []

for i in range(chance):
    while True:   
        letter = input("guess a letter: ")

        if len(letter) == 1:
            break
        else:
            print("please guess a letter")

    if letter in random_choice:
        print("you have guessed one letter correctly")
        guessed.append(letter)

    else:
        print("Incorrect guess")


    if (i-1) == 3:
        clue = input("will you want to have a clue: ")
        if clue.lower().startswith('y'):
            print("The first and last letter of the word is: ",hint)
        else:
            print("You are very confident: ")
        
print()
print("Lets see how much you have guessed the word: ")
print(f"You have guessed {len(guessed)} letters correctly and the letters are: ",guessed)   
print()
print("Now guess the whole word")

whole_word = input("Enter the whole word: ")

if whole_word == random_choice:
    print("Congratulations You got it !!!!")
else:
    print("Ahh, you lose :( ")

print()
input("Please press enter to leave the program")
