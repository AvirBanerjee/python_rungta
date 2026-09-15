# factorial
n=5
fact=1
for i in range(1,n+1):
    fact*=i # fact = fact *i
    print(f"factorial value at {i} interation is {fact}")
print(f"final value is {fact}")