age=25

if age <=0:
    print("Invalid")
else:
    if age<13:
        print("Child")
    elif age>=13 and age <=19:
        print("Teenager")   
    elif age>= 20 and age<=59:
        print("Adult")
    elif age>=60 and age <=134:
        print("Senior")
    else:
        print("NOt possible")    
                  