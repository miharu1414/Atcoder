n =int(input())
a  = list(map(int,input().split()))
num = [0]*401
for i in range(n):
    num[a[i]+200] += 1
    
ans = 0
for i in range(401):
    for j in range(i,401):
        if i == j:
            continue
        ans += num[i]*num[j]*((i-200)-(j-200))**2        
print(ans)
