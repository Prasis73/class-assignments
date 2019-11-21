'''from calculator import name
print(name) ''' #linked with file calculator

#from calculator import * will import all file
#import calculator is a dual import       #to import name   print(calculator.prasis)
'''import calculator
print(calculator.prasis)'''

#for date and time
'''import datetime as dt
import time
print((dt.date.today()))
print('Formatted Time:',time.asctime())

print(dt.date.today())'''

#importing math
'''import math
num=int(input("enter number"))
print("factorial:", math.factorial(num))
print("suqare of given number is",math.sqrt(num))
print("value of sin",num,":",math.sin(num))'''

#for color
'''from termcolor import colored, cprint
text = colored('Prasis', 'red')
print(text)
cprint('i am a python programmer', 'blue', 'on_green')'''

#renaming file
'''import os
os.rename('file.txt','myfile.txt')  #source,destination'''



import numpy as np
a= np.array([[1,2,3],[3,4,5]])
print(a)
print(a.shape)
print(a[0,1])

