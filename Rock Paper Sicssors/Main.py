import random as rn  

trials = ['rock','paper','sicssor']
c_computer = 0
c_player = 0

print("Rock Paper Sicssors Game")
name = input("Enter your name: ")
print("Welcome to the game: ",name)

while True: 

    user = input("Enter your play (Rock,Paper or Sicssor) or PRESS 'q' to exit the game: ")
    computer = rn.choice(trials)

    if(computer == 'rock' and user.lower()== 'paper'):
        print(f"computer choose: {computer} and you chose: {user}")
        print("Player Wins")
        c_player+=1

    elif (computer == 'rock' and user.lower() == 'rock'):
        print(f"computer choose: {computer} and you chose: {user}")
        print("Tied....")

    elif(computer == 'rock' and user.lower() == 'sicssor'):
        print(f"computer choose: {computer} and you chose: {user}")
        print("Computer Wins")
        c_computer+=1

    elif (computer == 'paper' and user.lower() == 'paper'):
        print(f"computer choose: {computer} and you chose: {user}")
        print("Tied....")

    elif(computer == 'paper' and user.lower() == 'sicssor'):
        print(f"computer choose: {computer} and you chose: {user}")
        print("Player Wins")
        c_player+=1

    elif(computer == 'paper' and user.lower() == 'rock'):
        print(f"computer choose: {computer} and you chose: {user}")
        print("Computer Wins")
        c_computer+=1

    elif(computer == 'sicssor' and user.lower() == 'sicssor'):
        print(f"computer choose: {computer} and you chose: {user}")
        print("Tied....")

    elif(computer == 'sicssor' and user.lower() == 'rock'):
        print(f"computer choose: {computer} and you chose: {user}")
        print("Player Wins")
        c_player+=1

    elif(computer == 'sicssor' and user.lower() == 'paper'):
        print(f"computer choose: {computer} and you chose: {user}")
        print("Computer Wins")
        c_computer+=1

    elif(user.lower() == 'q'):
        print("Terminated game.......")
        print(f"Computer Score: {c_computer}  and {name} scored: {c_player} points")
        
        if c_computer > c_player:
            print("Computer Won")
        elif c_computer == c_player:
            print("Game tied...")
        else:
            print("Player Won")
        exit()
    
    else:
        print("Invalid Input Try again")

