s = input()

ans = []
for i in range(len(s)):
    ans.append(s[:i] + s[i:])
for i in range(len(s)):
    ans.append(s[i:]+s[:i])
ans.sort()
print(ans[0])
print(ans[len(ans)-1])