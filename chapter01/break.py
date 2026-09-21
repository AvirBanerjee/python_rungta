n=6
is_prime=True
for i in range(2,n):
    if n%i==0:
        is_prime=False
        break
    print(i)
    print(is_prime)
# if is_prime:
#     print("Prime number")
# else:
#     print("not prime")            