s = input()
t = input()
ok = 1
if len(s) > len(t):
    print("No")
    exit()
for i in range(len(s)):
    if (s[i]!=t[i]):
        ok = 0
if ok:
    print("Yes")
else:
    print("No")
