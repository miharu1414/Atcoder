k = int(input())

now = 7
i = 1
ans = -1
while i <= 10**6:
    if now % k == 0:
        ans = i
        break
    now = (now * 10 + 7)%k 
    i+=1
print(ans)