n= int(input())
p = list(map(int,input().split()))
pre = [-1] * (n+1)

for i in range(n-1):
    pre[i+2] = p[i]
P = n
ans = 0
while True:
    P = pre[P]
    ans += 1
    if P == 1:
        break
print(ans)