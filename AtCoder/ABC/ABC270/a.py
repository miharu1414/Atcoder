a,b = map(int,input().split())
def solve(x,ans):
    if x == 1:
        ans[0] += 1
    if x == 2:
        ans[1] += 1
    if x == 3:
        ans[0] += 1
        ans[1] += 1
    if x == 4:
        ans[2]+=1
    if x == 5:
        ans[0] += 1
        ans[2]+=1
    if x == 6:
        ans[1]+=1
        ans[2]+=1
    if x == 7:
        ans[0]+=1
        ans[1]+=1
        ans[2] += 1
     
ans = [0,0,0]
solve(a,ans)
solve(b,ans)
A = 0
for i in range(3):
    if ans[i] > 0:
        if i ==0:
            A+=1
        if i ==1:
            A+=2
        if i == 2:
            A+=4
print(A)
