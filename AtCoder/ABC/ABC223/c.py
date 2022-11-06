n = int(input())
ab = [map(int,input().split()) for i in range(n)]
a,b = [list(i) for i in zip(*ab)]

left = 0
for i in range(n):
    left += a[i]/b[i]
left = left / 2
ans =0 
for i in range(n):
    if left > a[i]/b[i]:
        left -= a[i]/b[i]
        ans += a[i]
    else:
        ans += b[i]*left         
        break
print(ans)