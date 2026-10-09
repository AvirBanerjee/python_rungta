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

#code



count=1000#global

def outer_func():
    count=0 # enclosing
    # print(a)
    def inner_func():
        nonlocal count # local
        a=9
        count+=1
        print(count)
    inner_func()    
    inner_func()    
    inner_func()    

outer_func()

outer_func()



ice_creame=True #global
def check(score):
    pizza=True #local -> for check(fucn)
    
    if score > 75:
        global ice_creame
        ice_creame=56
        print(pizza)
        print(ice_creame)
    else:
        return None

check(89)

# pizza
ice_creame=False
  


