n=int(input("Enter the number:"))
print("Prime numbers:")
for i in range(2,n):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i,end=" ")
