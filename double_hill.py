n=int(input("Enter number of rows:"))

for i in range (n+1):
    for j in range(1,2*n):
        if j<=i or j>=2*n-i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
  
