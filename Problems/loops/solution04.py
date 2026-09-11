# sum of n natural no.
# n=10
# total=0
# for i in range(1,n+1):
#     total=total+i
#     print(f"value of total is {total} in interation number {i}")

# odd or even
# n=20
# sum_even=0
# for i in range(1,n+1):
#     if i%2==0:
#         sum_even=sum_even+i 
# print("sum of even numbers is",sum_even)        
# sum_odd=0          
# for i in range(1,n+1):
#     if i%2!=0:
#         sum_odd=sum_odd+i  
# print("sum of odd numbers is",sum_odd)        

# # factorial
# n=5
# fact=1
# for i in range(1,n+1):
#     fact*=i # fact = fact *i
#     print(f"factorial value at {i} interation is {fact}")
# print(f"final value is {fact}")    


#factor
n=6
total=0
for i in range(1,n):
    if n%i==0:
        total+=i
        print(f"In place factor number {i} value of total is {total}")
if total==n:
    print("perfect number")
else:
    print("Not perfect number")        

