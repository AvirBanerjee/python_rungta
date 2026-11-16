class Car:
    def __init__(self,userbrand,usermodel): # contsructor called automatically when object is created
        self.brand=userbrand #car_01.name="Toyota",car_02.brand="Hyundai",car_03.barnd="Honda"
        self.model=usermodel#car_01.model="Corola",car_02.model="verna",car_03.model="city"

        # print("Yes I am a contructor")

car_01=Car("Toyota","Corola") # equal to Car.__init__(car_01,"Toyota","Corola")
car_02=Car("Hyundai","Verna") # equal to Car.__init__(car_01,"Toyota","Corola")
car_03=Car("Honda","City") # equal to Car.__init__(car_01,"Toyota","Corola")

print(car_01.brand,car_01.model)
print(car_02.brand,car_02.model)
print(car_03.brand,car_03.model)
