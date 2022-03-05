name = input("Username : ")
age = int(input('Age : '))

print(f"Hello {name}!")

def checkMail():
    email = input("Enter your email : ")
    print(f"Pls check your email : {email}")
    checkmail = input("Right? (y/n) : ")
    return checkmail

if age >= 18: 
    print('You are adult. You can save money in our bank')

    cond = True
    while(cond==True):
        a = checkMail()
        if a == 'y' or a == 'Y': 
            cond = False
        elif a == 'n' or a == 'N':
            continue
        else: 
            print("Wrong input, pls enter only 'y' or 'n'.")
            checkMail()
        print("Congratulation....Well Done!")


else: 
    print("Sorry, you cann't save your money because you are too young")



