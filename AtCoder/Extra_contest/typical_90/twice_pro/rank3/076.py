from bisect import bisect


n = int(input())
a = list(map(int,input().split()))
length = [0]*(2*n+1)
sum = sum(a)

for i in range(2*n):
    length[i+1] = length[i] + a[i%n]

length.sort()

import bisect
for i in range(2*n+1):
    now = length[i]

    x = bisect.bisect_left(length,sum/10 + length[i])
    if x ==2*n+1:
        continue
    if (length[x]-length[i])==sum/10:

        print("Yes")
        exit()
print("No")