# def add(arr):
#     arr.append(100)
# def subtract(x):
#     x-=10
#     return x


# # x=10

# lst=[1,2,3,4,5,6,7]
# print("before add():",lst)
# add(lst)
# print("after add():",lst)

# x=20
# print("Before subtract():",x)
# print(subtract(x))
# print("After subtract():",x)



# count=0 #global scope
# def increment():
#     a=10 #local
#     global count
#     count =count +1
# increment()
# print(count)

count=0 #global
def outer_func():
    count=0 # enclosing
    def inner_func():
        nonlocal count # local
        count+=1
        print(count)
    inner_func()    
    inner_func()    
    inner_func()    

outer_func()







