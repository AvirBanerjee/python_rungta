class employe:
    # def __init__(self): # default
    #     print("I am contructor")
    # def __init__(self,name): #Parameterized
    #     self.name=name
    #     print("I am Parameterized constructor")
    def __init__(self,name,salary=None):
        self.name=name #Instance Variables ->employe_01.name
        if salary!=None:
            self.salary=salary

    def working(self): #method
        print(f"{self.name} is working")

    def greet(self):
        print("heloo")    

    # def __del__(self): #Destructor
    #     print("object deleted")   


employe_01=employe("ashutosh","100k")
employe_02=employe("avir")
employe_01.working()
employe_01.greet()
employe_02.working()
print(isinstance(employe_01,employe))
print(hasattr(employe_01,"score"))
print(employe_01.name)
print(employe_01.__dict__)