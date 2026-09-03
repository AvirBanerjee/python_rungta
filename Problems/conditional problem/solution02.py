# age=16
# price= 12 if age>=18 else 8

# is_Wednesday=True
# if(is_Wednesday):
#     print("price on discount:",price-2)
# else:
#     print("Nhi milega discount:",price)    

age=int(input("Enter your age:"))
day=int(input("Enter 1 if wed else enter 0"))
is_Wednesday=None
if day==0:
    is_Wednesday=False
else:
    is_Wednesday=True 

price= 12 if age>=18 else 8

if(is_Wednesday):
    print("price on discount:",price-2)
else:
    print("Nhi milega discount:",price)
