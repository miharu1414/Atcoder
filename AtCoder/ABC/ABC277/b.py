n = int(input())
s = [input() for i in range(n)]

kinds = set()
for S in s:
    kinds.add(S)
s1 = "HDCS"
s2 = "A23456789TJQK"
ok = 1
for i in range(n):
    if s[i][0] in s1 and s[i][1] in s2:
        continue
    else:
        ok = 0
        break

if len(kinds) != n:
    ok = 0
if ok:
    print("Yes")
else:
    print("No")