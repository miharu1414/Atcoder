h,w = map(int,input().split())
a = []
for i in range(h):
    x = list(map(int,input().split()))
    a.append(x)
row = [0]*h
col = [0]*w
for i in range(h):
    row[i] = sum(a[i])
for i in range(w):
    for j in range(h):
        col[i]+= a[j][i]

for i in range(h):
    ans = []
    for j in range(w):
        ans.append(row[i]+col[j]-a[i][j])
    print(*ans)