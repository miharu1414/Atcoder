n ,a , b = map(int,input().split())
s = input()
ori_s = s
new_s  = s + s
cost = 10**20
k = 0
for i in range((n-1)//2,3*n//2):
    mid = i
    if n&1:
        cnt = 0
        for j in range(n//2):
            if new_s[j+mid-n//2] != new_s[mid+n//2-j]: cnt += 1
        cost = min(cost,cnt*b+k*a)
    else:
        cnt = 0
        for j in range(n//2):
            if new_s[j+ mid - n//2+1] != new_s[mid + n//2 -j ]: cnt += 1
        cost = min(cost,cnt*b+k*a)
    
    
    k+=1
print(cost)