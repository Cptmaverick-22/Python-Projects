title = "ATM MACHINE"
print(title.center(25, "*"))

details = {}
fields = 3

for i in range(fields):
    if i == 0:
        key = "Name"
        value = input("Enter Your Name: ")
        details[key] = value
    if i == 1:
        key = "PIN"
        value = input("Enter Your PIN: ")
        details[key] = int(value)
    if i == 2:
        key = "Balance"
        value = input("Enter the Balance: ")
        details[key] = int(value)
print(details)

total_amount = 0

print("Details stored.....")
print()

choice = input("Do you want to use ATM? ")

if choice.lower().startswith('y'):

    while True:  
        name_check = input("Enter Your Name: ")

        if name_check == details["Name"]:
            while True:
                pin_check = int(input("Enter your PIN: "))
                if pin_check == details["PIN"]:
                    print("""Press 1 for deposit \n2 for withdraw \n3 for checking balance""")

                    while True:
                        user = input("Enter your choice or press 'q' to exit: ")

                        if user == '1':
                            amount = int(input("Enter the amount you want to deposit: "))
                            details['Balance'] += amount

                        if user == '2':
                            amount = int(input("Enter the amount you want to withdraw: "))
                            if details['Balance'] >= amount:
                                details["Balance"] -= amount
                                print(f"{amount} withdrawn")
                            else:
                                print("Insufficient funds")

                        if user == '3':
                            print("Available Balance: ", details["Balance"])

                        if user == 'q':
                            print("Available Balance: ", details["Balance"])
                            exit()

                else:
                    print("Incorrect PIN. Try again.")
            break  
        else:
            print("This account is not present in the database. Try again.")  

else:
    exit()
