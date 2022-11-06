a = list(map(int,input().split()))
ans = [0]*4
for i in range(2):
    for j in range(2):
        ans[2*i+j] = a[i]*a[j+2]
print(max(ans))
