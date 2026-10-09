print("Welcome to Calculator")
def sum(a,b):
    return a+b
def Subtract(a,b):
    return a-b
def Prod(a,b):
    return a*b
def divide(a,b):
    return a/b
val=int(input("Enter 0 to start nad enter -1 to end"))
if val==0:
    acitve=True
    current=-1
    while(acitve):
        print("1 Sum")
        print("2 Subtaract")
        print("3 Multiply")
        print("4 Divide")
        current=int(input("Enter the number of opertaion to be performe"))
        if current==1:
            num1=int(input("ENTER THE FIRST VALUE"))
            num2=int(input("ENTER THE SECOND VALUE"))
            print(sum(num1,num2))
            
        elif current==2:
            num1=int(input("ENTER THE FIRST VALUE"))
            num2=int(input("ENTER THE SECOND VALUE"))
            print(Subtract(num1,num2))
        elif current==3:
            num1=int(input("ENTER THE FIRST VALUE"))
            num2=int(input("ENTER THE SECOND VALUE"))
            print(Prod(num1,num2))
        elif current==4:
                    num1=int(input("ENTER THE FIRST VALUE"))
                    num2=int(input("ENTER THE SECOND VALUE"))
                    print(divide(num1,num2))    

else:
    exit()    