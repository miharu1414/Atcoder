# https://atcoder.jp/contests/abc266/tasks/abc266_f

n = int(input())

G =[[] for i in range(n)]
for i in range(n):
    u,v = map(int,input() ) 
    u -= 1
    v -= 1
    G[v].append(u)
    G[u].append(v)


from collections import deque 

deq = deque()


root  = [-1] * n
for i in range(n):
    if len(G[i]) == 1:
        deq.append(i)
        root[i] = i




while len(deq):
    now = deq.popleft()

    for next_v in G[now]:
        if len(G[next_v]) - 1 == 1:
            deq.append(next_v) 
            root[next_v] = root[v]



