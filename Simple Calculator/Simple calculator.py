def add(num1,num2):
    return num1+num2
    
def sub(num1,num2):
    return num1-num2

def mul(num1,num2): 
    return num1*num2

def div(num1,num2):  
    return num1/num2

print("Press '1' for addition Press '2' for Subtraction Press '3' for Multiplication Press '4' for Division")

while True:  

    choice = input("Enter your choice or press 'q' to end the program:  ")

    if choice == '1':

        num1 = int(input("Enter the 1st number: "))
        num2 = int(input("Enter the 2nd number: "))
        print("Addition of {num1} and {num2}: ",add(num1,num2))

    elif choice == '2':

        num1 = int(input("Enter the 1st number: "))
        num2 = int(input("Enter the 2nd number: "))
        print("Subtractin of {num1} and {num2}: ",sub(num1,num2))

    elif choice == '3':

        num1 = int(input("Enter the 1st number: "))
        num2 = int(input("Enter the 2nd number: "))
        print("Multiplication of {num1} and {num2}: ",mul(num1,num2))

    
    elif choice == '4':

        num1 = int(input("Enter the 1st number: "))
        num2 = int(input("Enter the 2nd number: "))
        print("Division of {num1} and {num2}: ",div(num1,num2))


    elif choice == "q":
        print("Program Terminated..")
        exit()

    