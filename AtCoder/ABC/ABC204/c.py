# スタックオーバーフローを防ぐ
import sys
sys.setrecursionlimit(10 ** 6)

n, m =map(int,input().split())
a,b = [],[]
for i in range(m):
    A,B = map(int,input().split())
    a.append(A)
    b.append(B)

Graph = [[] for i in range(n+1)]

parent = [-1]*(n+1)
for i in range(m):
    Graph[a[i]].append(b[i])

def up_cnt(x,seen):
    if x in seen:
        return 0
    seen.add(x)
    ans = 0
    for new_x in Graph[x]:
        ans += up_cnt(new_x,seen)
    ans += 1
    return ans
ans = 0

for i in range(1,n+1):
    seen = set()
    ans += up_cnt(i,seen)
print(ans)
    