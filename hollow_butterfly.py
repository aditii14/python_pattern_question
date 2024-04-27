n=int(input("enter the number of rows:"))
for i in range (1,n):
    for j in range(1,n):
        if j==1 or j==n-1:
            print("*",end=" ")
        elif i==j or j==n-i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()