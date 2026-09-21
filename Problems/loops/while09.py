n = int(input("Enter number: "))


while n >= 10:
    total = 0

    while n > 0:
        total += n % 10
        n //= 10

    n = total

print("Single digit =", n)