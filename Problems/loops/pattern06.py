n = 5

for i in range(1, n + 1):
    # spaces
    for j in range(n - i):
        print(" ", end="")
    # increasing numbers
    for j in range(2*i-1):
        print("*", end="")
    print()    
for i in range(n,0,-1):
    # spaces
    for j in range(n - i):
        print(" ", end="")
    # increasing numbers
    for j in range(2*i-1):
        print("*", end="")
    print()     
    