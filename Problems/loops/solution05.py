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