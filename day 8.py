#to make notepad
'''f=open("file.txt","w")
text=input("write until you type quit ")
while text!='quit':
    f.writelines(text +'\n')
    text=input()
print("saving......")
f.close()'''

#to read files
'''with open("file.txt","r") as f:
    text=f.read()
print(text)'''

#to append file    // to write replace a with w
'''f=open("file.txt","a")
f.writelines("\n above statements are false")
f.close()'''


#to change
'''f=open("file.txt",'w+')
f.writelines("hahahha lol i am a good")
f.seek(6)
f.writelines("everyone")
f.close()'''

#Write a program to find prime number from 1 to 2500 using comprehension
'''list_com=[x for x in range(1,2500)]
for x in list_com:
    if x > 1:
        for i in range(2, x):
            if (x % i) == 0:
                break
        else:
            print(x,"\t",end="")'''



#write a program to convert farenheight to celsius using map
'''list1=[23,54,67]
list=list(map(lambda x:(x-32)*5/9,list1))
print(list)'''


#program that copies content of one file to another
'''with open("file.txt") as f:
    with open("file1.txt", "w") as f1:
        for line in f:
            f1.write(line)'''

#file that edits
#ERROR_DONT KNOW
'''with open("file.txt", "r+") as f:
    old = f.read()  # read everything in the file
    for i in old:
        if [i]=="-":
            
    f.seek(6)  # rewind
    f.write(" " + old)  # write the new line before '''

#using comprehenssion to get prime number
lst=[x for x in range (0,100) for y in range(2,100) if x%y!=0]
print(lst)
'''list_com=[x for x in range(1,2500)]
for x in list_com:
    if x > 1:
        for i in range(2, x):
            if (x % i) == 0:
                break
        else:
            print(x,"\t",end="")'''