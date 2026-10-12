# def sum(*vir):
    # # print(type(args))
    # # print(args)
    # lenght=len(args)
    # sum=0
    # # print(lenght)
    # for i in range(0,lenght):
    #     sum+=args[i] # i=0->i=>1=>i=>2=>i=3 
    #     # print(args[i])
    # return sum    
    # for el in vir:
    #     sum+=el
    # return sum    

# result=sum(6,7,8,9)    
# 
# result=sum()
# print(result)


# def user_Info(**kuchbhii):
#     for name,fullname in kuchbhii.items():
#         print(name,fullname)

# result=user_Info(name="avir",Email="ashutosh.banerjee@microsoft.com",employed=True) 
# print(result)   

def student_report(name, *subjects, **details):
    print("Name:", name)
    print("Subjects:", subjects)
    print("Other details:", details)

student_report("Ravi", "Python", "Math","EVS", grade="A", age=20)