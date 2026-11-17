class Student:
    college="rungta" #class variable
    def __init__(self,name,email,rollno): 
        self.name=name
        self.email=email
        self.rollno=rollno

stu_01=Student("vipin","vipin@rungta.org",456892)
stu_02=Student("nitin","nitin@rungta.org",456893)
stu_01.college="xyz"
print(stu_01.college)
print(stu_02.college)
