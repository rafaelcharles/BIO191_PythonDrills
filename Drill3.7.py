#Drill3.7
N = int(input("Enter an integer for the side length of diamond: "))

if N > 0:           
    for i in range(N):
        for s in range (N - i) :
            print(" ", end="")
        for j in range((i * 2) - 1):
            print("*", end="")
        print()
    for i in range(N, 0, -1):
        for s in range (N - i) :
            print(" ", end="")
        for j in range((i * 2) - 1):
            print("*", end="")
        print()

#Retrieved from https://stackoverflow.com/questions/32613579/creating-a-diamond-pattern-using-loops