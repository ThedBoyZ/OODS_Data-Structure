print("*** Fun with Drawing ***")
num = int(input("Enter input : "))
row = 1 + (num-1)*4
col = 1 + (num-1)*4
middle = int(round((row/2),0))+1
for i in range(row):
    for j in range(col):
        if i == 0 or i== row-1:
            print("#",end="")
        elif i < middle:
            if j==0 or j == col-1:
                print("#",end="")
            elif i%2 == 0 and j>=i and j<=(col-i)-1:
                print("#",end="")
            elif i>2 and i>=j and j<=(col-i)-1 and j%2==0 or i>2 and i+j>=col and j%2==0:
                print("#",end="") 
            elif i == middle-1 and j == middle-1:
                print("#",end="")
            else:
                print(".",end="")
        elif i >= middle:
            if j==0 or j == col-1:
                print("#",end="")
            elif i%2 == 0 and j>=(row-i)-1 and j<=(col-(row-i)):
                print("#",end="")
            elif i>2 and i>=j and j<=(col-i)-1 and j%2==0 or i>2 and (row-i)+j>=col and j%2==0:
                print("#",end="") 
            else:
                print(".",end="")
    print("")
