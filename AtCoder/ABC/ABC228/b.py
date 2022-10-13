n,x = map(int,input().split())
a = list(map(int,input().split()))
a.insert(0,-1)
ans = [0]*(1+n)
i = x
ans[i] = 1
num = 1
while num<n:
    i = a[i]
    if ans[i] == 1:
        break 
    ans[i] = 1
    num+=1
print(sum(ans))
    
    