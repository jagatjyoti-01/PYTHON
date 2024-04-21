# try except 

a=int(input("enter your age"))
print(a+3)      # if here an user enter a invalid age(like jagat) then it show an error and next line ot exicutated

try:
    a=int(input("enter your age"))
    print(a+3)
except:
    print("some error occour")       # if valid input then then try block is exicute other wise except

# if want to know which type of exception then 
try:
    a=int(input("enter your age"))
    print(a+3)
except Exception as e:
    print("some error occour",e) 

