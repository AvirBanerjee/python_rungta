# type Conversion - > changing datatype
# two type 
# 1 Implicit Type Conversion 

a=5
b=7.5
sum=a+b
print(sum) # 12.5 
print(type(sum))

# 2 Explicit Type Conversion (Type Casting) .

# example
val1=input("Enter first value :")  #5
val2=input("Enter second value :") #5
# sum2=val1+val2                     
sum2=int(val1)+int(val2)                     
print(sum2)                        #55
# print(type(sum2))# str
print(type(sum2))# int

# example
val3=int(input("Enter first value :"))  #5
val4=int(input("Enter second value :")) #5

sum3=val3+val4
print(sum3)
print(type(sum3))

#example
Temp=5.6
temp=int(Temp)
print(type(temp))

#eample
score="15"
Score=int(score)
print(type(Score))

#example
temprature="15.6"
Temprature=float(temprature)
print(Temprature)