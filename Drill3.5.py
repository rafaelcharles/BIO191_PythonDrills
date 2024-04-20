#Drill3.5
rows = 11
columns = 20

for i in range(1,rows):
    for j in range(1,columns):
        if j == 1:                  
            print(i, end="")
        elif j == 3:             
            print(i*2, end="")
        elif j == 5:             
            print(i*3, end="")
        elif j == 7:      
            print(i*4, end="")
        elif j == 9:      
            print(i*5, end="")
        elif j == 11:      
            print(i*6, end="")
        elif j == 13:      
            print(i*7, end="")
        elif j == 15:      
            print(i*8, end="")
        elif j == 17:      
            print(i*9, end="")
        elif j == 19:      
            print(i*10, end="")
        else:                       
            print(" ", end="")
    print("")