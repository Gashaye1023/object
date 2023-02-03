class employee():
    def __init__(self,name,age,id,salary):  
        self.name = name 
        self.age = age
        self.salary = salary
        self.id = id
 
em = employee("Gashaye",22,1000,1234) 
em = employee("Adugna",23,2000,2234)
print(em.__dict__)