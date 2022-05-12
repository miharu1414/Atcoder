n = int(input())
a = list(map(int,input().split()))
from collections import deque
deq = deque()
count = 0

for i in range(n):
    if not deq:
        deq.append([a[i],1])
        count+=1
        print(count)
        continue
    nakami = deq.pop()
    if nakami[0] == a[i]:
        if nakami[1] == a[i]-1:
            count-=a[i]-1
            pass
        else:
            nakami[1] += 1
            deq.append(nakami)
            count+=1
    else:
        deq.append(nakami)
        deq.append([a[i],1])
        count+=1
    
    print(count)
