n,m = map(int,input().split())

a = [list(map(int,input().split())) for i in range(n)]

import itertools 



com = list(itertools.permutations(range(m), 2))

ans = 0
for i in com:
    x,y= i
    count = 0
    for j in range(n):

        count += max(a[j][x],a[j][y])    
    ans = max(ans,count)
print(ans)
    