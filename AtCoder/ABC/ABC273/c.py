n = int(input())
a = list(map(int,input().split()))


c = set(a)
b = list(c)
num = len(b)
b.sort()
import bisect
ansa = [0]*(n+1)
for i in range(n):
    ans = bisect.bisect(b,a[i])
    ansa[num-ans] += 1
for i in range(n):
    print(ansa[i])