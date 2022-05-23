n = int(input())
a = list(map(int,input().split()))

a.sort()
a_map = dict()
for i in range(n):
    if a[i] not in a_map:
        a_map[a[i]] = 0
    else: 
        a_map[a[i]] +=1 

kaburi = n - sum(list(a_map.values()))

from operator import mul
from functools import reduce

def cmb(n, r):
    if n - r < r: r = n - r
    if r == 0: return 1
    if r == 1: return n

    numerator = [n - r + k + 1 for k in range(r)]
    denominator = [k + 1 for k in range(r)]

    for p in range(2,r+1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p-1,r,p):
                numerator[k - offset] /= pivot
                denominator[k] /= pivot

    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= int(numerator[k])

    return result

count  = 0
kaburi = n
count = cmb(n,3)
for ka in a_map.values():
    if ka != 0:
        ka +=1  
        count -= cmb(ka,2)*(n-ka) - cmb(ka,3) 
print(count)