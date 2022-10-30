l,r = map(int,input().split())


cnt = 0
for x in range(l,r+1):
    div = r // x 
    cnt = cnt + (r+1 - x - div)
print(cnt)

