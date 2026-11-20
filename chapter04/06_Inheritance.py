class Parent: # base class or parent class
    def __init__(self,eye_color,hair_color):
        self.eye_color=eye_color
        self.hair_color=hair_color
    def greet(self):
        print("Hello")    

class Child(Parent): # derived or child class
    def __init__(self,eye_color,hair_color,height):
        super().__init__(eye_color,hair_color)
        self.height=height


parent_01=Parent("brown","black")
child_01=Child(parent_01.eye_color,parent_01.hair_color,"5.8")
child_01.greet()