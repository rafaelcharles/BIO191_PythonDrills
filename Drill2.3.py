#Drill2.3
x = int(input("Please enter an integer:"))
y = int(input("Please enter another integer:"))
z = int(input("Please enter a third integer:"))

if x%2 != 0 and x > y > z:
    print(x, ' is the greatest.')
elif y%2 != 0 and y > z > x:
    print(y, ' is the greatest')
elif z%2 != 0 and z > y > x:
    print(z, ' is the greatest')
elif x%2 != 0 and y%2 == 0 and z%2 == 0:
    print(x, ' is the greatest.')
elif x%2 == 0 and y%2 != 0 and z%2 == 0:
    print(y, ' is the greatest.')
elif x%2 == 0 and y%2 == 0 and z%2 != 0:
    print(z, ' is the greatest.')
elif x%2 != 0 and y%2 != 0 and z%2 == 0 and x > y:
    print(x, ' is the greatest.')
elif x%2 != 0 and y%2 != 0 and z%2 == 0 and x < y:
    print(y, ' is the greatest.')
elif x%2 != 0 and y%2 == 0 and z%2 != 0 and x > z:
    print(x, ' is the greatest.')
elif x%2 != 0 and y%2 == 0 and z%2 != 0 and x < z:
    print(z, ' is the greatest.')
elif x%2 == 0 and y%2 != 0 and z%2 != 0 and y < z:
    print(z, ' is the greatest.')
elif x%2 == 0 and y%2 != 0 and z%2 != 0 and y > z:
    print(y, ' is the greatest.')
elif x%2 == 0 and y%2 == 0 and z%2 == 0:
    print('None of the integers are odd.')