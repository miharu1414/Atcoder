n, k = map(int,input().split())
s = input()

ans_s = ''
num = 0
for i in range(n):
    if num < k:
        if s[i] == 'o':
            ans_s += 'o'
            num+=1
        else:
            ans_s += 'x'
            
    else:
        ans_s += 'x'
print(ans_s)