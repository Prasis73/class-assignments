#to find area of circle
'''def rad(a):
    return (22/7)*a*a

a=int(input("enter the radius"))
ans=rad(a)
print(ans)'''

#function to return power
'''a=int(input("enter the value"))
b=int(input("enter the power"))
def pow(a,b):
    return a**b
ans=pow(a,b)
print(ans)'''


#To check armstrong number
num = int(input("Enter a number: "))
a= num
def arm(num):
    sum=0
    a=num
    f=len(num)
    while a > 0:
        b = a % 10   #remainder gives last digit
        sum += b ** 3    #adds the last digit cube with sum
        a //= 10        # divides the input data and gives intiger value
    return sum
sum=arm(num)
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")



# to check palindrome
'''num=int(input("Enter a number:"))
def pal(num):
    c = 0
    while(num>0):
          b=num%10      #Gives last digit
          c=c*10+b      #adds last digits in c (makes reverse)
          num=num//10   #deducts last digit and gives int value
    return c
a=pal(num)
if(num==a):
    print("palindrome")
else:
    print("not palindrome")'''