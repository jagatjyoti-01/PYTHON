#oops concept


class Employee:
    def __init__(self ,name,salary):
        self.name=name
        self.salary=salary

    def getSalary(self):
        print(self.salary)

v=Employee("raju","8677")
print(v.salary)
print(v.name)
v.getSalary()

vv=Employee("mohan","778")
print(vv.name)
print(vv.salary)
vv.getSalary()