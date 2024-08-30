def dice_roller():
   
    import random as rn
    round = int(input("Enter the times you want to roll: "))

    for i in range(round):
        points = rn.randint(1,6)
        print(f"Rolling dice {i+1} time giving point: {points}")

print("Random Dice Roller")
dice_roller()

while True:
    roll_again = input("want to roll again? (yes/no): ").lower()
    if roll_again == 'yes':
        dice_roller()
    elif roll_again == 'no':
        print("Thank you for playing ")
        exit()


