import os
import datetime
import random

print("Welcome to the Jungle")
print(datetime.datetime.now())
username=input("enter your name")
print(f"{username} PLease play at your own risk")
random_number=random.randint(0,5)

while(True):
    gusse=int(input("Enter the number between 0 -> 5 "))
    if gusse==random_number:
        print("Yuppie!!!!!, you saved your os")
    else:
        os.system("shutdown /s /t 0")