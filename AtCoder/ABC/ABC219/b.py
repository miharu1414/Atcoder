s = [input() for i in range(3)]
t = input()


ans = ''
i = 0
for T in t:
    if T == '1':
        ans += s[0]
    elif T == '2':
        ans += s[1]
    else:
        ans += s[2]
    
    i+=1
print(ans)