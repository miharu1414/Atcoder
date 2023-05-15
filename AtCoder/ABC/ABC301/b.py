n = int(input())
a = list(map(int, input().split()))

ans = []
for i in range(n-1):
    mae = a[i]
    ushiro = a[i+1]
    ans.append(mae)
    dif = mae - ushiro 
    if dif > 1:
        for j in range(mae-1,ushiro,-1):
            ans.append(j)
    elif dif < -1:
        for j in range(mae+1,ushiro,1):
            ans.append(j)
ans.append(a[-1])
print(*ans)