s = input()
ans = 0
i = 0
sign = 0
while i<len(s):
    if s[i] == '0' and sign == 1:
        sign = 0
        
    elif s[i] == '0' and sign == 0:
        sign = 1
        ans += 1
    else:
        ans += 1
        sign = 0
    i+=1
print(ans)
         