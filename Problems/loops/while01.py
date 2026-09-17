n=1440
sum=0
while n >0 :
    digit=n%10
    sum+=digit
    n//=10
print ("Sum of numbers in a digit are:",sum)    