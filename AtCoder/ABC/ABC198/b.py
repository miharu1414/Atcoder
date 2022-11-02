s = input()
gyaku = len(s)-1
for i in range(len(s)):
    if s[len(s)-i-1] != '0':
        break
    gyaku -= 1
idx = 0
for i in range(len(s)):
    if s[i] != '0':
        break
    idx += 1
ok = 1
while idx <= gyaku:
    if s[idx] != s[gyaku]:
        ok = 0
        break
    idx += 1
    gyaku -= 1
if ok:
    print("Yes")
else:
    print("No")