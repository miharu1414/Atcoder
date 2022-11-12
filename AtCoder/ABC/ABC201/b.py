n = int(input())
st = [map(str,input().split()) for i in range(n)]
s,t = [list(i) for i in zip(*st)]


ans = []
for i in range(n):
    ans.append([int(t[i]),s[i]])
ans.sort(reverse=True)
print(ans[1][1])