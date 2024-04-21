#file manage or read, write ,append file
s="i am just a sentence which enter into file by a process"

with open("lec16.txt","w")as f:  #context manager   # w is write mode   # it is automaticaly close 
    f.write(s)

# another mathhod
fp=open("lec16_b.txt","w")
fp.write(s)
fp.close()    # it requre a colse method to close

#to read the data 
fr=open("lec16.txt","r")
v=fr.read()
print(v)

with open("lec16.txt","r")as f:
    v=f.read()
    print(v)

# append a file

with open("lec16-c.txt","a")as f:    # a for append mode
 f.write("here you can add more numner of  sentence but privious sentence is not delete but in wite operation if dd any new sentence the old sentece is delete")


