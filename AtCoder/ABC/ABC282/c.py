n = int(input())
s = input()

sign = 0
ans = ''
for i in range(n):
    if s[i] == '"' and sign == 0:
        sign = 1
        ans+=s[i]
    elif s[i] == '"' and sign == 1:
        sign = 0
        ans+=s[i]
    elif s[i] == ',' and sign == 0:

        ans += '.'
    else:
        ans += s[i]
print(ans)