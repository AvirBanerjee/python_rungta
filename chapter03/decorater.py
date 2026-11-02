def isLoggedIN(func): #decorator
    def wrapper():
        print("Before the function runs.")
        func()
        print("After the function runs.")
    return wrapper


@isLoggedIN
def show_dasboard():
    print("showing dasboard")

# user_status=True

# isLoggedIN(user_status,show_dasboard)
# # print(result)
result=show_dasboard()
print(result)




