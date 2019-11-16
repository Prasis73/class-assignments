#To get correct name age and phone no

name=input("enter your first name")
lname=input("Enter your last name")
while name.isalpha()==False or name.count("")<=4 or lname.isalpha()==False or lname.count("")<=4:
    print("Invalid name!! must be string and should be more than 3 char")
    name = input("enter your name")
    lname= input("Enter your last name")
    continue
    if name.isalpha()==True and name.count("")>=4 and lname.isalpha()==True and lname.count("")>=4:
        break
age=input("enter your age")
age1=int(age)
while age.isalpha() == True or age1<18:
    print("age must be greater than 18")
    age = input("enter your age")
    age1 = int(age)
    continue
    if age.isalpha()==False or age1>18:
        break
phone=input("enter your phone number")
while phone.isalpha()==True and phone.count("")!=10:
    Print=("Invalid phone number!!")
    phone = input("enter your phone number")
    continue
    if phone.isalpha()==True and phone1.count("")==10:
        break
print("Name= {} {}\nAge= {}\nPhone number= {}".format(name,lname,age1,phone))