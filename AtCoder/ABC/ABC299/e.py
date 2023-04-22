n,m = map(int,input().split())
u,v =[],[]
G = [[] for i in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())

    G[a-1].append(b-1)
    G[b-1].append(a-1)
    

k = int(input())
p,d =[],[]
for i in range(k):
    a,b = map(int,input().split())
    p.append(a-1)
    d.append(b)
s = [0]*(n+1)
possible = [[-1,-1] for i in range(n+1)]

if k ==0:
    ans = '1'
    for i in range(n-1):
        ans += '0'
    print("Yes")
    print(ans)
    exit()
     
white = set()
import collections
black = collections.defaultdict(list)
for i in range(k):
    now = p[i]
    
    
        # 最初の頂点集合 (スタートは頂点 0 のみ)
    nodes = [0]

    # 各頂点が何手目に探索されたか
    # -1 は「まだ探索されていない」ことを表す
    dist = [-1] * (n+1)

    # k 手目に探索された頂点集合を格納 (最大でも N-1 手まで)
    nodes = [[] for i in range(d[i]+2)]

    # 頂点 0 を始点とする
    dist[now] = 0
    nodes[0] = [now]
    if d[i]!=0:
        white.add(p[i])
    # k 手目の探索をする
    ok = 1
    if d[i]!=0:
        ok = 0
    for k in range(1, d[i]+1):
        # k-1 手目に探索された各頂点 v に対して
        for v in nodes[k - 1]:
            # 頂点 v から 1 手で行ける頂点 next_v を探索
            for next_v in G[v]:
                if k == d[i]:
                    ok = 1
                # 頂点 next_v が探索済みであれば何もしない
                if dist[next_v] != -1:
                    continue
                if k != d[i]:
                    white.add(next_v)
                # 頂点 next_v を探索する
                dist[next_v] = dist[v] + 1
                nodes[k].append(next_v)
    if ok == 0:
        print("No")
        exit()
    for j in nodes[d[i]]:
        black[i].append(j)

for i in black:
    flag = 0
    for j in black[i]:
        if j not in white:
            flag = 1
            s[j] = 1
    if flag == 0:
        print("No")
        exit()
print("Yes")
ans = ''
for i in range(n):
    ans += str(s[i])
print(ans)
     