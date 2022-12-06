s = input()
t = input()
ans = len(t)-1
for i in range(len(s)):
    if s[i] != t[i]:
        ans = i 
        break
print(ans+1)