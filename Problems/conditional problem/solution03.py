score=101

if score >= 101:
    print("Invalid score")
    exit()

if score >=90:
    grade='A'
elif score>=80:
    grade='B'
elif score>=70:
    grade='C'
elif score >=60:
    grade='F'
else:
    print("Invalid")    

print("Grade:",score)