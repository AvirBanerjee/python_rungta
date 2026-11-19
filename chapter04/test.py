class Student:
    college="rungta"  #class variable
    def __init__(self,name,rollno,email,branch):
        self.name=name #instance variable
        self.rollno=rollno
        self.email=email
        self.branch=branch
    def show(self):
        print(f"{self.name} {self.email} {self.branch}  {self.rollno} {self.college}" )
    @classmethod
    def greet(Student):
        print("HEllooo")   
    @staticmethod
    def double(n):
        print(n*2)         

student_01=Student("Vir",300607,"vir@gmail","CSE")
student_02=Student("RIV",300607,"vir@gmail","CSE")
student_03=Student("ASHUTOSH",300607,"vir@gmail","CSE")
student_04=Student("Shiv",300607,"vir@gmail","CSE")
student_05=Student("VISH",300607,"vir@gmail","CSE")
Student.greet()
Student.double(6)
student_01.college="xyz"
student_01.show()
student_02.show()
student_03.show()
student_04.show()

