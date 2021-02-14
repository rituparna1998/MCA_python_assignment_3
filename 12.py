n=int(input("Enter the number:"))
i=0
j=1
s=0
print(i,j,end=" ")
for s in range(2,n):
    s=i+j
    i=j
    j=s
    print(s,end=" ")

