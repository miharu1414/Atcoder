n = int(input())
s = input()
count_o = 0
count_x = 0

if n == 1:
    print(0)
    exit()
if s[0] == 'o':
    count_o = 1
else:
    count_x = 1
ans = 0

i = 0
k = 0
while 1:
    while count_o * count_x <= 0:
        k+=1
        if k>=n:
            break
        if s[k] == 'o':
            count_o +=1
        else:
            count_x += 1
        
    if count_o * count_x > 0:
        ans += n - k
    
    i+=1

    if s[i-1] == 'o':
        count_o -=1
    else:
        count_x -= 1
    if i == n:
        break

print(ans)