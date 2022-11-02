r, x, y = map(int,input().split())

import math
r1 = math.sqrt(x**2+y**2)

if r > r1:
    print(2)
    exit()
for i in range(1,10**6):
    if r* i >= r1:
        print(i)
        exit()