n = int(input("Enter number: "))
digit = int(input("Enter digit: "))

count = 0

if n == 0 and digit == 0:
    count = 1

while n > 0:
    if n % 10 == digit:
        count += 1
    n //= 10

print("Frequency =", count)