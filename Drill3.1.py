Drill3.1
asterisk = int(input("Enter a number:"))
number = 1
while number <= asterisk:
    for j in range(0,cnt):
        print("*", end="")
        if (j != number):
            print(" ", end="")
    number = number + 1
    print()