from queue import Queue

n,m = map(int,input().split())
G = [[] for i in range(n)]
for i in range(m):
    a,b = map(int,input().split())
    G[a].append(b)
    G[b].append(a)

dist = [-1] * n

# queueを使用して探索する頂点を管理する
que = Queue()

dist[0] = 0
que.put(0)

while not que.empty():
    # queueの要素を取り出す
    v = que.get()

    for next_v in G[v]:
        if dist[next_v] != -1:
            continue

        # 頂点next_vを探索する
        dist[next_v] = dist[v] + 1
        que.put(next_v)

