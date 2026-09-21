n = int(input("Enter number: "))
original = n
reverse = 0

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n //= 10

if abs(original) == reverse:
    print("Palindrome")
else:
    print("Not a palindrome")