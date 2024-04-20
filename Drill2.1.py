#Drill2.1
x = int(input("What is your age?"))
y = input("Do you have a fishing license in MN (yes/no) ?")
z = input("Does your parent have a fishing license (yes/no)")

if x >= 18 and y == "yes" or x < 18 and z == "yes":
    print("You are legal to fish in MN.")
else:
    print("You are not legal to fish in MN.")