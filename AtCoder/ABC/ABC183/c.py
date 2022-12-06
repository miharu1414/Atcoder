n, k = map(int,input().split())
t = [list(map(int,input().split())) for i in range(n)]

arr = [i+1 for i in range(n-1)]
import itertools
per = list(itertools.permutations(arr))
cnt = 0
for l in per:
    ans = 0
    before = 0
    for now in l:
        ans += t[before][now]
        before = now
    ans+= t[before][0]
    if ans == k:
        cnt += 1
print(cnt)