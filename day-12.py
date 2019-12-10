#Dictionary
'''dict_name={
    'name':'prasis',
    'age':21,
    'place':'Itahari'
}

print(dict_name['name'])
print(dict_name['age'])
dict_name['age']=22
print(dict_name['age'])

for x in dict_name.values():
    if x=='prasis':
        print("matched")

for y in dict_name.keys():
    print(y)'''


#Regular Expression

import re
'''text='prasis my name is rijal praisi'
pattern='^p.....'
find=re.match(pattern,text)
if find:
    print("matched at ",find.start())
    print("the word matched is",find.group(0))
else:
    print("not found")'''

'''text='prasis my name is rijal praisi'
pattern='^p.....'
find=re.search(pattern,text)
if find:
    print("matched at ",find.start())
    print("the word matched is",find.group(0))
else:
    print("not found")'''
####################
'''
text=input("input text")
pattern=input("what you want to search?")
find=re.match(pattern,text)
if find:
    print("matched at ", find.start())
    print("the word matched is", find.group(0))
else:
    print("no match found")'''

'''
dict_name={
    'name':input("name: "),
    'age':input("age: "),
    'place':input("address: ")
}

for x in dict_name.values():
    if x==input("enter value you want to search"):
        print("matched")
    else:
        print("not found")'''




#Checking email
'''import re
regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
def check(email):
    if (re.search(regex, email)):
        print("Valid Email")
    else:
        print("Invalid Email")
if __name__ == '__main__':
    email = input("Enter your email")
    check(email)'''

# Creating an empty Dictionary
Dict = {}

# Adding elements one at a time
Dict[0] = input("enter value")
Dict[2] = input("enter value")
Dict[3] = input("enter value")
print("\nDictionary after adding 3 elements: ")
print(Dict)


