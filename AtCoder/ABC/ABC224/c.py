n = int(input())
xy = [map(int,input().split()) for i in range(n)]
x,y = [list(i) for i in zip(*xy)]

import math
def dis(x1,y1,x2,y2):
    return math.sqrt((x2-x1)**2 + (y1-y2)**2)
count = 0
for i in range(n):
    for j in range(i,n):
        for k in range(j,n):
            dx1 =  (x[i] - x[j])
            dx2 = (x[i] -x[k])
            dy1 =  (y[i] - y[j])
            dy2 =  y[i] - y[k]
            if dx2 * dy1 == dx1 * dy2:
                continue
            else:
                count += 1
print(count)