#function

def greethlo():
    print("this is function")
    print("this is function")
    print("this is function")
    print("this is function")
    print("this is function")
    print("this is function") 

print("function exicuting ..")
greethlo()


def greethlo(name, ending):
    print("this is function")
    print("this is function")
    print(name,ending)
    print("this is function")
    print("this is function")
    print("this is function")
print("this is paramiter fun")
greethlo("jagat","dash")

def latterganerator(name,date):
    st=f"hii,mam \n this is {name} and i will not come to school on {date}"   #\n is new line   
     # here f is use to write variable into string
    print(st)
latterganerator("jagat dash",20)

#return funcction
def avarage(a,b):
    return(a+b)/2

print(avarage(3,4))