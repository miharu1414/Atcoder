n = int(input())
mod = n
ans = 0
S = set()
ok = 1
for i in range(n):
    ans = (i+ans)%mod
    if ans in S:
        ok = 0
        break
    else:
        S.add(ans)
if ok:
    print(*list(range(n)))
    exit()
ans = 0
S = set()
ok = 1
A = []
for i in range(n,0,-1):
    if i == n:
        i = 0
    ans = (i+ans)%mod
    if ans in S:
        ok = 0
        break
    else:
        A.append(i)
        S.add(ans)
if ok:
    print(*A)
else:
    print(-1)