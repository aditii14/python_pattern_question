n=int(input("Enter the nuber of rows: "))
for i in range (n+1):
    for j in range(2*n+1):
        if j<=n-i or j>=n+i :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()