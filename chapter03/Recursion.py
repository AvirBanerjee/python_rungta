import sys
# def show(x): #5 -> 4 -> 3 -> 2 -> 1
#     if x==0: #base
#         print("Done")
#         return
#     else:
#         print("value of",x) # 5  4  3  2  1 
#         show(x-1) # recurcive call 
#             # 1. 5 - 1 = 4
#             # 2. 4 - 1 = 3
#             # 3. 3 - 1 = 2
#             # 4. 2 - 1 = 1
#             # 5. 1 - 1 = 0    

# n=5
# show(n)

# def fact(x):
#     if x==1:
#         return 1
#     return x * fact(x-1)


# n=5
# print(fact(5))

def fact(n):
    if n==1: #base case
        print("Base case reached")
        return 1
    print("Number of call:",n)
    return n*fact(n-1) #recursive call

x=990
result=fact(x) # final call
print(result)

# print(sys.getrecursionlimit())