n=int(input("Enter number of rows:"))

for i in range (n+1):
    for j in range(2*n+1):
        if j<=i or j>=2*n-i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
  