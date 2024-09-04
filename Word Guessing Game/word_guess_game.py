import random as rn

def checking(letter):
    whole_word = input("Enter the whole word: ")

    if whole_word == random_choice:
        print("Congratulations You got it !!!!")
    else:
        print("Ahh, you lose :(  The correct word was: ",random_choice)

    print()
    input("Please press enter to leave the program")

words = ['hello','dog','apple','class','orange','melon','straw','game','word','elephant','good','marvel','disney']

random_choice = rn.choice(words)                 #print(random_choice)
hint = random_choice[0]+random_choice[-1]        #print(hint) this is used to view the hint

name = input("Enter your name: ")
print()

print("Welcome to word game",name)
print()

print("You will have 6 chances to guess the word")
print()
print()

chance = 6
guessed = []
correct_guess = {}
counting = 0

for i in range(chance):
    while True:   
        letter = input("guess a letter or type 'quit' to guess the complete word: " )

        if len(letter) == 1:
            break
        if letter == "quit":
            checking(letter)

        else:
            print("please guess a letter")

    if letter in random_choice:
        count = random_choice.count(letter)
        counting +=1
        

        if letter not in correct_guess:
            correct_guess[letter] = 0
            counting = 0
        
        if correct_guess[letter] <= count: 
            correct_guess[letter]+=1
            guessed.append(letter)
            print(f"You have guessed one letter correctly! '{letter}' appears {counting + 1 } Time")
        else:
            print("You have already guessed maximum of this letter")
    
    else:
        print("Incorrect guess")


    if (i) == 3:
        clue = input("will you want to have a clue: ")
        if clue.lower().startswith('y'):
            print("The first and last letter of the word is: ",hint)
            print("The length of the word is: ",len(random_choice))
        else:
            print("You are very confident: ")
        
print()
print("Lets see how much you have guessed the word: ")
print(f"You have guessed {len(guessed)} letters correctly and the letters are: ",guessed)   
print()
print("Now guess the whole word")

checking(letter)
