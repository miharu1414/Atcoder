n = int(input())
xy = [map(int,input().split()) for i in range(n)]
x,y = [list(i) for i in zip(*xy)]


import math
ans = 0
pair = dict()
for i in range(n):
    for j in range(n):
        if i == j :
            continue
        X,Y = x[i] - x[j],y[i]-y[j]
        gcdxy = math.gcd(X,Y)
        if (X//gcdxy,Y//gcdxy) not in pair:
            pair[(X//gcdxy,Y//gcdxy)] = 1
            ans +=1
print(ans)
