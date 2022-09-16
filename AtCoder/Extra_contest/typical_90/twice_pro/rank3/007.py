n = int(input())
a = list(map(int,input().split()))
q = int(input())
b = [int(input())for i in range(q)]
a.sort()


import bisect
for i in range(q):
    pos = bisect.bisect_left(a,b[i])
    if pos>0 and n != 1 and pos != n:
        ans = min(abs(a[pos]-b[i]),abs(a[pos-1]-b[i]))
    elif pos == n:
        ans  = abs(a[pos-1]-b[i])
    else:
        ans = abs(a[pos]-b[i])
    print(ans)
    