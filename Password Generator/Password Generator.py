import random as rn
import string as st
spe_char = '!@#$%^&*<>,.-+?_'
password =[]
print("Password generator: ")  
length = int(input("Enter the length of the password you want: "))         
user_choice = input("Enter the difficulty of your password (EASY) (MEDUIM) (HARD): ").lower()

if user_choice == 'easy':
    password.append(rn.choice(st.ascii_uppercase))
    for i in range(length-1):
        password.append(rn.choice(st.ascii_lowercase+ st.digits))

elif user_choice == 'medium':
    password.append(rn.choice(spe_char))
    for i in range(length-1):
        password.append((rn.choice(st.ascii_lowercase + st.ascii_uppercase + st.digits)))

elif user_choice == 'hard':
    for i in range(length):
        password.append(rn.choice(st.ascii_uppercase + st.ascii_lowercase + st.digits + spe_char))

else:
    print("invaid choice.......")
    exit()

rn.shuffle(password)
password_str = ''.join(password)
print("The generated password is: ",password_str)

        
