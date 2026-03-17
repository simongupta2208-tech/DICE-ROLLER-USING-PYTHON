import random
print("wellcome to dice roller simulator")
choice="yes"
while choice == "yes":
    a=random.randint(1,6)
    print("you rolled",a)
    choice = input("do you want to roll again(yes/no)")
else:
    print("thank you for playing")
