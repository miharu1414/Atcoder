x,y,n = map(int,input().split())
ans = 10**6
for i in range(101):
    for j in range(101):
        if x*i + y * j <= ans and i + 3*j == n:
            ans =  x*i + y * j
print(ans)