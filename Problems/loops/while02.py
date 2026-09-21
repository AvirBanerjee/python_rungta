n = int(input("Enter number: "))
n = abs(n)
count = 0

if n == 0:
    count = 1
else:
    while n > 0:
        count += 1
        n //= 10

print("Number of digits =", count)