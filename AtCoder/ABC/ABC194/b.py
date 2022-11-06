from cmath import inf


n = int(input())
ab = [map(int,input().split()) for i in range(n)]
a,b = [list(i) for i in zip(*ab)]

ans_1 = inf
idx1 = 0
idx2 = 0
for i in range(n):
    
    for j in range(n):
        if i != j:
            ans_1 = min(ans_1,max(a[i],b[j]))
        else:
            ans_1 = min(ans_1,a[i]+b[j])
    
        
print(ans_1)