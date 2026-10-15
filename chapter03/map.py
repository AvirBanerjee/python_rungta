lst=[4,6,78,6,7,8,6]
# def cube(x):
#     return x**3
# new=[]
# for item in lst:
#     new.append(cube(item))

new=list(map(lambda x:x**3,lst))
print(new)