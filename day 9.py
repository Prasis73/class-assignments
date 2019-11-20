'''class LowAgeError(Exception):
    def _init_(self):
         super(LowAgeError, self)._init_("age should be greater")
class prasis(Exception):
    def __init__(self):
        super(prasis,self).__init__("lol")

age=int(input("enter age"))
if age<18:
    raise LowAgeError
elif age==19:
    raise prasis
else:
    print("accepted")'''

#user defined error to check length of string
class NumberError(Exception):
    def _init_(self):
         super(NumberError, self)._init_("should be 3 string")
name=input("name?")
if name.count("")<=3:
    raise NumberError
else:
    print("correct")
