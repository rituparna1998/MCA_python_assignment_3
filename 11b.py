for i in range(4):
    for j in range(7):
        if j>=i and j<=6-i:
            print("O",end="")
        else:
            print(" ",end="")
    print()
