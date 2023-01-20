n = int(input())
xy = [map(int,input().split()) for i in range(n)]
x,y = [list(i) for i in zip(*xy)]

z,w = [0]*n,[0]*n
for i in range(n):
    z[i] = x[i] + y[i]
    w[i] = x[i] - y[i]

z.sort()
w.sort()
ans = 0
ans = max(abs(z[0]-z[n-1]),abs(w[0]-w[n-1]))
print(ans)