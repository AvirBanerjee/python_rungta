from functools import reduce
def sum(a,b):
    return a+b
lst=[3,4,5,6,5,6,7,5,7,8]
print(reduce(sum,lst))
