n = int(input())
s = input()
flag = 1
ans = -1
renzoku = 0
ok = 0
for i in range(n):
    if s[i] == '-':
        if ok == 0:
            ok = 1
            ans = max(ans,renzoku)
            renzoku = 0
        else:
            ans = max(ans,renzoku)
            ok = 1
            renzoku = 0
    elif s[i] == 'o':
        renzoku += 1
        if ok == 1:
            ans = max(ans,renzoku)

if ans == 0:
    ans = -1
print(ans)