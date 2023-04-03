import time
from itertools import permutations
from collections import Counter


def f3(data):
    n = len(data)
    result = []
    cnt = Counter(data)
    keys = cnt.keys()

    def r(x,i=0):
        if i == n:
            result.append(x)
        else:
            for k in keys:
                if cnt[k] >= 1: # 残あり
                    cnt[k] -= 1
                    r([*x, k], i=i+1)
                    cnt[k] += 1
    r([])
    return result


h, w = map(int,input().split())
a = [list(map(int,input().split())) for i in range(h)]

from itertools import permutations
s = []
for i in range(h-1):
    s.append(0)
for i in range(w-1):
    s.append(1)


st = f3(s)
routes = sorted(st)
ans = 0
for route in routes:
    val = set()
    i,j = 0,0
    flag = 1
    val.add(a[i][j])
    for s in route:
        if s == 0:
            i += 1
        else:
            j += 1
        if a[i][j] in val:
            flag = 0
            break
        else:
            val.add(a[i][j])
    if flag:
        ans += 1
print(ans)