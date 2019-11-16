#multiplication
'''num = int(input("Enter the number: "))

print("Multiplication Table of", num)
for i in range(1, 11):
   print(num,"X",i,"=",num * i)'''



#enter number add in a list
'''List = []
n = int(input("Enter the list size :"))
for i in range(0, n):
    print("Enter number or string at location", i, ":")
    item = input()
    List.append(item)
print("List is ", List)'''


#from list make new list containing even number
'''list1=[]
List = []
n = int(input("Enter the list size :"))
for i in range(0, n):
    print("Enter number at location", i, ":")
    item = int(input())
    List.append(item)
print("List is ", List)
b=0
for a in List:
    if a%2==0:
        b=b+1
        list1.append(a)
print("list of even number is:",list1)'''


# to remove from a list and print remaining
'''List=[]
n=int(input("enter the list size"))
for i in range(0,n):
    print("Enter the number in list :")
    item = input()
    List.append(item)
print("list is",List)
List.pop(int(input("enter value you want to pop")))
print(List)'''

#seperate int srt and float from given list
import sys
List=[]
list1=[]
list2=[]
list3=[]
List = ['prasis',2.6,5,7,'sisarp']
print("list is",List)
for x in List:
    if type(x)==int:
        list1.append(x)
    elif type(x)==float:
        list2.append(x)
    elif type(x)==str:
        list3.append(x)
    else:
        sys.exit("unclassified")
print("integers:",list1)
print("floats:",list2)
print("strings:",list3)






