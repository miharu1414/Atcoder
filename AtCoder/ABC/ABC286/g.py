n , m = map(int,input().split())
u,v  =[],[]
G = [[] for i in range(n)]
for i in range(m):
    a,b = map(int,input().split())
    u.append(a-1)
    v.append(b-1)
k = int(input())
x = list(map(int,input().split()))

# 入力としてグラフG, Sを受け取る
def can_traverse_graph(G, S):
    # グラフGからSに含まれない辺を除く
    for edge in S:
        G.remove_edge(edge)
    # グラフGがEulerianグラフか判定
    if not is_eulerian(G):
        return False
    # Eulerian Pathを求める
    path = find_eulerian_path(G)
    # Sに含まれる辺がpathに含まれているか判定
    for edge in S:
        if edge not in path:
            return False
    return True

# グラフGがEulerianグラフか判定する関数
def is_eulerian(G):
    for vertex in G.vertices:
        if G.degree(vertex) % 2 != 0:
            return False
    return True