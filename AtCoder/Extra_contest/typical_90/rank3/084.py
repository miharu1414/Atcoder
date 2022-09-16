n = int(input())
s = input()

i, j = 0,1
count_o = 0
count_x = 0
ans = 0
if n == 1:
    print(0)
    exit()
if s[i]=='o':
    count_o+=1
else:
    count_x +=1
if s[j]=='o':
    count_o += 1
else:
    count_x += 1  
while i<len(s):
    while j<len(s):
        if count_o > 0 and count_x > 0:
            break
        j+=1
        if j == len(s):
            break
        if s[j]=='o':
            count_o += 1
        else:
            count_x += 1
    
    ans += len(s)-j
    if s[i]=='o':
        count_o-=1
    else:
        count_x -=1
    i+=1
print(ans)