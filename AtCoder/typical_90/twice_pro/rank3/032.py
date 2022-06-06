n = int(input())
a = [list(map(int,input().split())) for i in range(n)]
m = int(input())
G = [[1 for i in range(n)] for j in range(n)]
for i in range(m):
    x,y = map(int,input().split())
    G[x-1][y-1] = -1
    G[y-1][x-1] = -1


member = [i for i in range(n)]
import itertools
ans = []
ans_count = 0
for junban in itertools.permutations(member,n):
    count = 0
    flag = 1
    for i in range(n):
        count += a[junban[i]][i]
        if i!= n-1 and G[junban[i]][junban[i+1]]==-1:
            flag = 0
            break
    if flag:
        ans_count += 1
        ans.append(count)
if ans_count==0:
    print(-1)
    exit()
ans.sort()
print(ans[0])

