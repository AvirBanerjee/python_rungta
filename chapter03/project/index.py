import pyfiglet
import cowsay

print(pyfiglet.figlet_format("Buckshot"))
print(pyfiglet.figlet_format("roullet"))

cowsay.cow("Welcome to the jungle!!!")

print("Enter your name :")
name=input()
cowsay.cow(f"{name} Are u ready?")


