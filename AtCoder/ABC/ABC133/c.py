l, r = map(int,input().split())

M = 2019
mod = [0]*2019
for i in range(l,r+1):
    if mod[i%M] == 1:
        break
    mod[i%M] += 1

ans = 10**10
for i in range(2019):
    for j in range(i+1,2019):
        if mod[i]&mod[j]:
            ans = min(ans,i*j%M)
print(ans)