n, k = map(int,input().split())
ab =[map(int,input().split()) for i in range(n)]
a,b = [list(i) for i in zip(*ab)]

point = []
for i in range(n):
    point.append(b[i])
    point.append(a[i]-b[i])
point.sort(reverse=True)
ans  = 0
for i in range(k):
    ans += point[i]
print(ans)