s = input()

ans = ['' for i in range(len(s))]
for i in range(len(s)//2):
    ans[2*i] = s[2*i+1]
    ans[2*i+1] = s[2*i]

Ans = ''
for s in ans:
    Ans += s
print(Ans)