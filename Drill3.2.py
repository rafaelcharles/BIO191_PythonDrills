#Drill3.2
rows = 3
columns = 5

for y in range(0,rows) :
    for x in range(0,columns) :
        if x%2 == 0:
            print("*", end="")
        else: 
            print("-", end="")
    print()