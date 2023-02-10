n,k = map(int,input().split())
s = [input() for i in range(n)]
ans = []
for i in range(min(n,k)):
    ans.append(s[i])
ans.sort()
for i in range(min(n,k)):
    print(ans[i])