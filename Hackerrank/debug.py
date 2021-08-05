q,bribe = [1,2,3,5,4,6,7,8],0
for i,j in enumerate(q):
    for k in range(max(j-1,0),i):
        if q[k] > j:
            bribe += 1
            print(bribe)
    if j-i > 2:
        print('Too chaotic')