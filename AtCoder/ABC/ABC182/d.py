n = int(input())
a = list(map(int,input().split()))

idou = [0]*(200001)


max_idou = [0]*200001
maxr = 0
ans = 0
now = [0]*200001
for i in range(n):
    if i == 0:
        idou[i]=a[i]  


    else:
        now[i] = now[i-1] + idou[i-1]
        idou[i]=a[i]+idou[i-1]        
        max_idou[i] = max(max_idou[i-1],idou[i-1])
        
now[n] = now[n-1] + idou[i]
for i in range(n):
    if i == 0:  
        ans = max(ans,idou[i])
    
    else:
        ans = max(ans,now[i]+max_idou[i])
ans = max(ans,now[n])
print(ans)