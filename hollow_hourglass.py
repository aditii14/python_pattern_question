n=int(input("enter the number of rows:"))
for i in range (1,n):
    for j in range(1,n):
        if i==1 or i==n-1:
            print("*",end=" ")
        elif i==j or i==n-j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()