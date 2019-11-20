print("***********Welcome***********")
print("At first Enter the following details")
name=input("Enter your first name")
lname=input("Enter your last name")
while name.isalpha()==False or name.count("")<=4 or lname.isalpha()==False or lname.count("")<=4:
    print("Invalid name!! must be string and should be more than 3 char")
    name = input("enter your firstname")
    lname= input("Enter your last name")
    continue
    if name.isalpha()==True and name.count("")>=4 and lname.isalpha()==True and lname.count("")>=4:
        break
age=input("enter your age")
age1=int(age)
while age.isalpha() == True or age1<18:
    print("invalid!! age must be string and greater than 18")
    age = input("enter your age")
    age1 = int(age)
    continue
    if age.isalpha()==False or age1>18:
        break
phone=input("enter your phone number")
while phone.isalpha()==True or phone.count("")!=11:
    Print=("Invalid phone number!!")
    phone = input("enter your phone number")
    continue
    if phone.isalpha()==False and phone1.count("")==10:
        break



print(" Enter + for addition           Enter 's' to find simple interest\n Enter - for subtraction        Enter'b' for decimal to binary  \n Enter * for multiplication   \n Enter / for division        ")

operation = input("")
'''num1 = int(num3)
num2 = int(num4)'''
if operation == '+':
    num3 = input("enter frst integer number ")
    num4 = input("enter 2nd integer number ")
    while num3.isalpha() == True or num4.isalpha() == True:
        print("invalid!! must be integer")
        num3 = input("enter frst number ")
        num4 = input("enter 2nd number ")
    num1 = float(num3)
    num2 = float(num4)
    print('Hello {} {} your result is:\n {} + {}'.format(name,lname,num1, num2))
    print(num1 + num2)
elif operation == '-':
    num3 = input("enter frst integer number ")
    num4 = input("enter 2nd integer number ")
    while num3.isalpha() == True or num4.isalpha() == True:
        print("invalid!! must be integer")
        num3 = input("enter frst number ")
        num4 = input("enter 2nd number ")
    num1 = float(num3)
    num2 = float(num4)
    print('Hello {} {} your result is:\n{} - {}'.format(name,lname,num1, num2))
    print(num1 - num2)
elif operation == '*':
    num3 = input("enter frst integer number ")
    num4 = input("enter 2nd integer number ")
    while num3.isalpha() == True or num4.isalpha() == True:
        print("invalid!! must be integer")
        num3 = input("enter frst number ")
        num4 = input("enter 2nd number ")
    num1 = float(num3)
    num2 = float(num4)
    print('Hello {} {} your result is:\n{} * {}'.format(name,lname,num1, num2))
    print(num1 * num2)
elif operation == '/':
    num3 = input("enter frst integer number ")
    num4 = input("enter 2nd integer number ")
    while num3.isalpha() == True or num4.isalpha() == True:
        print("invalid!! must be integer")
        num3 = input("enter frst number ")
        num4 = input("enter 2nd number ")
    num1 = float(num3)
    num2 = float(num4)
    print('Hello {} {} your result is:\n{} / {}'.format(name,lname,num1, num2))
    print(num1 / num2)
elif operation == 's':
    P = input("Enter Principle ")
    T = input("Enter Time ")
    R = input("Enter Rate")
    while P.isalpha() == True or T.isalpha() == True or R.isalpha()==True:
        print("invalid!! must be integer")
        P = input("Enter Principle ")
        T = input("Enter Time ")
        R = input("Enter Rate")
    num1 = float(P)
    num2 = float(T)
    num3 = float(R)
    print('Hello {} {} your result is:\n'.format(name,lname))
    print((num1*num2*num3)/100)
elif operation == 'b':
    num = input("enter decimal value")
    while num.isalpha() == True:
        print("invalid!! must be integer")
        num = input("enter decimal value")
        if num.isalpha() == False:
            break
    dec = int(num)


    def convert(n):
        if n > 1:
            convert(n // 2)
        print(n % 2, end='')


    convert(dec)

else:
    print("You have not typed a valid operator, Run the program again")

a=2
b=int(a)
while b>1:
    a=input("\nEnter 'Y' to continue and 'N' to exit")
    if a=='Y':
        print(
            " Enter + for addition           Enter 's' to find simple interest\n Enter - for subtraction        Enter'b' for decimal to binary  \n Enter * for multiplication   \n Enter / for division        ")

        operation = input("")

        if operation == '+':
            num3 = input("enter frst integer number ")
            num4 = input("enter 2nd integer number ")
            while num3.isalpha() == True or num4.isalpha() == True:
                print("invalid!! must be integer")
                num3 = input("enter frst number ")
                num4 = input("enter 2nd number ")
            num1 = float(num3)
            num2 = float(num4)
            print('Hello {} {} your result is:\n{} + {}'.format(name,lname,num1, num2))
            print(num1 + num2)
        elif operation == '-':
            num3 = input("enter frst integer number ")
            num4 = input("enter 2nd integer number ")
            while num3.isalpha() == True or num4.isalpha() == True:
                print("invalid!! must be integer")
                num3 = input("enter frst number ")
                num4 = input("enter 2nd number ")
            num1 = float(num3)
            num2 = float(num4)
            print('Hello {} {} your result is:\n{} - {}'.format(name,lname,num1, num2))
            print(num1 - num2)
        elif operation == '*':
            num3 = input("enter frst integer number ")
            num4 = input("enter 2nd integer number ")
            while num3.isalpha() == True or num4.isalpha() == True:
                print("invalid!! must be integer")
                num3 = input("enter frst number ")
                num4 = input("enter 2nd number ")
            num1 = float(num3)
            num2 = float(num4)
            print('Hello {} {} your result is:\n{} * {}'.format(name,lname,num1, num2))
            print(num1 * num2)
        elif operation == '/':
            num3 = input("enter frst integer number ")
            num4 = input("enter 2nd integer number ")
            while num3.isalpha() == True or num4.isalpha() == True:
                print("invalid!! must be integer")
                num3 = input("enter frst number ")
                num4 = input("enter 2nd number ")
            num1 = float(num3)
            num2 = float(num4)
            print('Hello {} {} your result is:\n{} / {}'.format(name,lname,num1, num2))
            print(num1 / num2)
        elif operation == 's':
            P = input("Enter Principle ")
            T = input("Enter Time ")
            R = input("Enter Rate")
            while P.isalpha() == True or T.isalpha() == True or R.isalpha() == True:
                print("invalid!! must be integer")
                P = input("Enter Principle ")
                T = input("Enter Time ")
                R = input("Enter Rate")
            num1 = float(P)
            num2 = float(T)
            num3 = float(R)
            print('Hello {} {} your result is:\n'.format(name, lname))
            print((num1 * num2 * num3)/100)
        elif operation == 'b':
            num=input("enter decimal value")
            while num.isalpha() == True:
                print("invalid!! must be integer")
                num = input("enter decimal value")
                if num.isalpha() == False:
                    break
            dec = int(num)


            def convert(n):
                if n > 1:
                    convert(n // 2)
                print(n % 2, end='')


            convert(dec)


        else:
            print("You have not typed a valid operator, Run the program again")

    elif a=='N':
        print("******   *   *     *       *   *     *  *      *    *      \n"
              "  *      *****    ****     * * *     **        *    *\n"
              "  *      *   *   *    *    *   *     *  *       * * *    ")
        break
    else:
        print("enter valid character")