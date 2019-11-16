#odd even
'''num=int(input("enter the value to check odd or even\n"))
if num==0:
    print("0")
elif num<0:
    print("provide positive data")
elif num%2==0:
        print("even")
else:
    print("odd")'''


#Check leap year
'''num=int(input("enter the year\n"))
a=num%4
if a==0:
    print("leap year")
else:
    print("not leap year")'''

##ask name age and mobine no
name=input("enter your first name\n")
name1=input("enter your last name\n")
a=len(name)
b=len(name1)
c=int(a)
d=int(b)
if name.isalpha()==True and name1.isalpha()==True and c>3 or d>3:
    age=input("enter your age\n")
    e = int(age)
    if age.isalpha()==False and e>18:
        phone=input("enter your phone no\n")
        f=len(phone)
        ph=int(f)
        if phone.isalpha()==False and f==10:
            print(name,name1,e,phone)
        else:
            print("enter correct mobile no")
    else:
        print("enter age more than 18")

else:
    print("enter alphabet more than 3 charater")
