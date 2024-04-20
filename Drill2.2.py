#Drill2.2
x = int(input("Please enter your age:"))
y = input("Are you a natural born citizen of the U.S. (yes/no)?")
z = int(input("How many years have you resided in the U.S.?:"))

allowed = True
if x < 35:
    allowed = False
if y == "no":
    allowed = False
if z < 14:
    allowed = False
if allowed:
    print("You can run for president of USA.")
else:
    print("You cannot run for president of USA.")