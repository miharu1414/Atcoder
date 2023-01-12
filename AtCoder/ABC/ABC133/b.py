n, d = map(int,input().split())
x = [list(map(int,input().split())) for i in range(n)]

import math
def distance(x,y):
    ans = 0
    for i in range(len(x)):
        ans += (x[i]-y[i])**2
    return int(ans)
cnt = 0
heihousu = set()
for i in range(300):
    heihousu.add(i*i)
for i in range(n):
    for j in range(i+1,n):
        if distance(x[i],x[j]) in heihousu:
            cnt += 1
print(cnt)