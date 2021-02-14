currNum = 1
r = 4  
stop = 2
for i in range(r):
    for column in range(1, stop):
        print(currNum, end=' ')
        currNum += 1
    print("")
    stop += 1