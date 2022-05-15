# https://atcoder.jp/contests/abc248/tasks/abc248_d
from xml.etree.ElementTree import QName


n = int(input())
a = list(map(int,input().split()))
Q = int(input())
pos = [[] for i in range(200001)]

for i in range(n):
    pos[a[i]].append(i+1)

import bisect
for i in range(Q):
    l,r,x = map(int,input().split())
    sum = bisect.bisect(pos[x],r) - bisect.bisect(pos[x],l-1)
    print(sum)

    