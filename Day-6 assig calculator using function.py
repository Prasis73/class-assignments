#Using function
def again():
    a=input("do you want to calculate again?")
    if a.upper()=='Y':
       calculate()
    elif a.upper()=='N':
        print("Thank you")
    else:
        again()
def calculate():
    print("welcome")
    num1=int(input("enter frst no "))
    num2=int(input("enter 2nd no "))
    print("Enter + for addition\n Enter - for subtraction\n Enter * for multiplication\n Enter / for division")
    operation=input("")
    if operation=='+':
        print('{} + {}'. format(num1,num2))
        print(num1+num2)
    elif operation=='-':
        print('{} - {}'.format(num1, num2))
        print(num1 - num2)
    elif operation=='*':
        print('{} * {}'.format(num1, num2))
        print(num1 * num2)
    elif operation=='/':
        print('{} / {}'.format(num1, num2))
        print(num1 / num2)
    else:
        print("You have not typed a valid operator, Run the program again")
    again()

calculate()



def again():
    a=input("do you want to calculate again?")
    if a.upper()=='Y':
       calculate()
    elif a.upper()=='N':
        print("Thank you")
    else:
        again()



