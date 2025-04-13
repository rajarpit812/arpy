agein = input("enter your age: ")
age=int(agein)
while age <= 0:
    print("not valid age: ")
    age=int(input("enter age again: "))
if age<18:
    print("Booooo!!! MINOR")
elif age >= 18 and age<65:
    print("woah bda hogya")
else:
    print("buddha lmao")
