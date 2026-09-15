n = int(input("How many numbers: "))
largest = -1
second_largest = -1
for i in range(n):
    num = int(input("Enter number: "))
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num
print("Largest =", largest)
print("Second largest =", second_largest)