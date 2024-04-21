# list method
l1=[23,54,65,65,"jagat"]
print(type(l1))     #list
print(l1)


#list is muatable  or changeable but string is not muatable
# l1.remove("jagat")
# l1.sort()    # error bcz diffrent datatype so by remove jagat it can sort the list
l1.pop()
print(l1)

l1.append(98)   #add elment at last
l1.extend([44,56,76,43])
# l1.clear()
print(l1.index(23))      # 0


