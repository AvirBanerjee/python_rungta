lst=[1,5,-7,8,-9,6,-4,6,4,8,-10]
def check(a):
    return a <= 0
new = list(filter(check,lst))
print(new)