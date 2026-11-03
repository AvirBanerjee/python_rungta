def generator():
    for i in range(0,5):
        # return i  #-> 0 datatype=int  
        yield i  

# print(type(generator()))
# generator()
for val in generator():
    print(val)