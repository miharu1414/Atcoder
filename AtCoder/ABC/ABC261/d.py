n,m = map(int,input().split())
x = list(map(int,input().split()))
cy = [map(int,input().split()) for i in range(m)]

c,y = [list(i) for i in zip(*cy)]
cy = []
point = dict()
for i in range(m):
    point[c[i]] = y[i]
    cy.append([c[i],y[i]])

cy.sort()
dp = [0] * n
for i in range(n):
    if i == 0:
        dp[0] = 0
    else:
        dp[i] = dp[i-1] + x[i]



ans = [[0]*(n+2) for i in range(n+2)]

for i in range(0,n):
    
    for j in range(0,i+1):
        bonus = 0
        if j + 1 in point:
            bonus = point[j+1]
        ans[i+1][j+1] = max(ans[i+1][j+1],ans[i][j]+x[i]+bonus)
        ans[i+1][0] = max(ans[i+1][0], ans[i][j])
print(max(ans[n]))
