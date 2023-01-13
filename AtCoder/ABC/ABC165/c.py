n, m, q = map(int,input().split())
a,b,c,d = [],[],[],[]
for i in range(q):
    x,y,z,m = map(int,input().split())
    a.append(x)
    b.append(y)
    c.append(z)
    d.append(m)

ans = 0
for i in range(2 ** m):
    bag = []
    total = 0
    A = [m]*n
    seen = [0]*n
    ok = 1
    score = 0
    for j in range(m):  # このループが一番のポイント
        if ((i >> j) & 1):  # 順に右にシフトさせ最下位bitのチェックを行う
            if seen[a[j]] == 0 and seen[b[j]] == 0:
                A[a[j]] = A[b[j]] - c[j]
                seen[a[j]] = 1
                seen[b[j]] = 1
                score += d[j]
            elif seen[a[j]] == 1 and seen[b[j]] == 0:
                A[b[j]] = A[a[j]] + c[j]
                seen[b[j]] = 1
                score += d[j]
            elif seen[a[j]] == 0 and seen[b[j]] == 1:
                A[a[j]] = A[b[j]] - c[j]
                seen[a[j]] = 1
                score += d[j]
            elif seen[a[j]] == 1 and seen[a[j]] == 1:
                if A[a[j]] != A[b[j]] - c[j]:
                    ok = 0
                    break
                else:
                    score += d[j]
    if ok == 1 and max(A) - min(A) <= m:
        ans = max(ans,score)
print(ans)
        