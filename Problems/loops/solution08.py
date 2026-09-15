n = 10
sum = 0
for num in range(2, n + 1):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count = count + 1
    if count == 2:
        sum = sum + num

print("Sum of prime numbers =", sum)