n, m = map(int,input().split())
a = list(map(int,input().split()))

ans = [0]*(n)
for i in range(m):
    ans[a[i]-1] = 1

j = 0

b = []
for i in range(n):
    if ans[i] == 0:
        for k in range(i,j-1,-1):
            b.append(k+1)
        j = i + 1 
print(*b)

    