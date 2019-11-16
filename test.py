'''num=int(input("enter decimalno"))
while num>=1:
    num = int(num // 2)
    a = (num*2) % 2
    print(a,end = '')

    if num<1:
        break'''
dec=int(input("dec"))
def convert(n):
   if n > 1:
       convert(n//2)
   print(n % 2,end = '')
convert(dec)






