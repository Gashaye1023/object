class Employee:
    def __init__(self,name, salary):
        self.name=name
        self.salary=salary
    def displyinfo(self):
       print("Name : ", self.name,  ", Salary: ", self.salary)
ob=Employee("Gashaye",10000)
ob.displyinfo()
