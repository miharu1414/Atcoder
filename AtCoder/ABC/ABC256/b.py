n = int(input())
a = list(map(int,input().split()))
masu = [0]*4

p = 0
import copy
for i in range(n):
    masu[0] += 1
    da = a[i]
    reset = [0]*4
    for j in range(4):
        if da+j >=4:
            p += masu[j]
        else:
            reset[da+j] = masu[j]
    masu = copy.copy(reset)
print(p)