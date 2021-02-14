n=int(input("Enter a number:"))
if(n%2!=0):
    for i in range(1,n+2):
        if(i%2!=0):
            print(" "*((n-i)//2),"O"*i)

else:
    n=n-1
    for i in range(1,n+2):
        if(i%2!=0):
            print(" "*((n-i)//2),"O"*i)
