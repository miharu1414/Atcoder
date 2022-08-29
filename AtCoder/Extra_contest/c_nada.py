from collections import deque
 
h, w, k = map(int, input().split())
a = []
 
for i in range(h):
    x = input()
    a.append(x)
 
 
dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]
 
maguma = deque([])
had = [[-1] * w for i in range(h)]
 
for i in range(h):
    for j in range(w):
        if a[i][j] == "#":
            had[i][j] = 0
        elif a[i][j] == "@":
            had[i][j] = 0
            maguma.append([i, j])
 
 
while maguma:
    x, y = maguma.popleft()
    for dx, dy in zip(dxs, dys):
        # 隣接マス
        x2, y2 = x + dx, y + dy
 
        # マス (x2, y2) が盤面外である場合、黒マスである場合はスキップ
        if x2 < 0 or x2 >= h or y2 < 0 or y2 >= w or had[x2][y2] != -1:
            continue
 
        # マス (x2, y2) を探索する
        had[x2][y2] = had[x][y] + k
        maguma.append([x2, y2])
 
 
dist = [[-1] * w for i in range(h)]
 
# todo リストを表すキュー
que = deque([])
 
# マス (X0, Y0) を始点とする
dist[0][0] = 0
que.append([0, 0])
 
 
# キューが空になるまで探索する
while que:
    # キューから頂点を取り出す
    x, y = que.popleft()
 
    # マス (x, y) から 1 手で行けるマスを順に探索
    for dx, dy in zip(dxs, dys):
        # 隣接マス
        x2, y2 = x + dx, y + dy
 
        # マス (x2, y2) が盤面外である場合、黒マスである場合はスキップ
        if x2 < 0 or x2 >= h or y2 < 0 or y2 >= w or (had[x2][y2] != -1 and had[x2][y2] <= dist[x][y] + 1):
            continue
        
        # マス (x2, y2) が探索済みであれば何もしない
        if dist[x2][y2] != -1:
            continue
 
        # マス (x2, y2) を探索する
        dist[x2][y2] = dist[x][y] + 1
        que.append([x2, y2])
        
 
if dist[h-1][w-1] != -1 and a[0][0] != "@":
    print("Yes")
else:
    print("No")