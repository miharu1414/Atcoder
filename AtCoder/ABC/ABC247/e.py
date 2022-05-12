from itertools import count
from os import NGROUPS_MAX
from threading import _RLock


n,x,y = map(int,input().split())
a = list(map(int,input().split()))

def shakutori(B):
    L,R = 0,0
    count_x,count_y = 0,0
    count = 0

    while L<len(B):
        while R<len(B) and (count_x==0 or count_y==0):
            if B[R]== x:
                count_x +=1
            if B[R] == y:
                count_y += 1
            R+=1
        if count_x > 0 and count_y > 0:
            count += len(B) - R + 1
        if B[L]==x:
            count_x-=1
        if B[L]==y:
            count_y-=1
        L+=1
    return count
ans = 0
i = 0
while i != n:
    B = []
    while i!=n and y<= a[i]<= x:
        B.append(a[i])
        i+=1
    
    if len(B)!=0:
        ans += shakutori(B)
    else:
        i+=1
print(ans)