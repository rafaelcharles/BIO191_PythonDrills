#Drill3.6
N = int(input("Enter an integer for the side length of the squares: "))

if N > 0:           
    for i in range(N):
        for a in range (N) :
            print("*", end="")
        print()
    for i in range(1,N+1):
        for j in range(1,N+1):
            if i == N or j == N or i == N//3 or j == N//3:
                print("x", end="")
            else:
                print("", end="")
        print()

#Retrieved from https://stackoverflow.com/questions/50090389/display-squares-of-asterisks-filled-and-hollow-side-by-side