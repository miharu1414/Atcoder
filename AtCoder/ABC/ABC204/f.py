n,m= map(int,input().split())
a,b,c,d= [],[],[],[]
for i in range(m):
    x,y,z,w = map(int,input().split())
    a.append(x)
    b.append(y)
    c.append(z)
    d.append(w)

node = [i for i in range(1,n+1)]
linkcost = {}
Chncost = {}
for i in range(m):
    linkcost[(a[i],b[i])] = c[i]
    Chncost[(a[i],b[i])] = d[i]
    
#{(リンクの起点，リンクの終点)：旅行時間}で表される有向リンクのdictionary．
link = list(linkcost.keys()) #linkcostのkeyからリンクのlistを生成．


#◆変数の準備----------------------------
startnode = 1 #始点ノード
inf = 1<<30  #距離無限大を意味する，十分に大きな数
dist = {} #そのノードまでの距離を表す変数をdictionaryで用意
prev_node = {} #あるノードに最短経路で向かう際の直前のノード

#distに初期値を与える
for i in node:
    dist[i] = inf #初期値は距離無限大
dist[startnode] = 0 #始点のみ距離0

#undecided_distを定義する．
undecided_dist = dist.copy() #最短距離が未確定のノードとその距離．
 #辞書関数はミュータブルなオブジェクトのため，copy()メソッドを用いて複製する．

#prev_nodeに初期値を与える
for i in node:
    prev_node[i] = None


#◆本計算-------------------------------------
while undecided_dist: #最短距離が未確定のノードがなくなるまで繰り返す．
    u = min(undecided_dist, key=undecided_dist.get) #最短距離が未確定のノードのうち，距離が最小のノードを取り出す．
    del undecided_dist[u] #取り出したノードは未確定のノードから削除．
    for i in range(len(link)): #各リンクについて，
        if link[i][0] == u: #リンクの起点が，今取り出しているノードである場合，
            v = link[i][1] #リンクの終点に関して，その点までの距離を確認していく．
            
            if (dist[v] > dist[u] + linkcost[u,v] + int(Chncost[u,v]/(Chncost[u,v]/2+1))+Chncost[u,v]//2): #当該リンクを利用した経路の方が短い場合，
                dist[v] =dist[u] + linkcost[u,v] + int(Chncost[u,v]/(Chncost[u,v]/2+1))+Chncost[u,v]//2 #距離を修正．
                prev_node[v] = u #そのノードに最短経路で向かう際の直前のノードを修正．

    
if dist[n] >= 1073741824:
    print(-1)
    exit()
print(dist[n])