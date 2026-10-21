# def show(x): #5 -> 4 -> 3 -> 2 -> 1
#     if x==0: #base
#         print("Done")
#         return
#     else:
#         print("value of",x) # 5  4  3  2  1 
#         show(x-1) # recurcive call 
            #1. 5 - 1 = 4
            #2. 4 - 1 = 3
            #3. 3 - 1 = 2
            #4. 2 - 1 = 1
            #5. 1 - 1 = 0    

# n=5
# show(n)

def fact(x):
    if x==1:
        return 1
    return x * fact(x-1)


n=5
print(fact(5))