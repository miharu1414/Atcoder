n = int(input())
s = list(map(int,input().split()))
ans  = [0]*n
wa = 0
for i in range(n):
    if i == 0:
        ans[i] = s[i]
        wa = s[i]
    else:
        ans[i] = s[i] - wa
        wa += ans[i]
print(*ans)