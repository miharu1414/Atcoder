def process_queries(N, queries):
    edges = [set for i in range(N)]
    connected = set()  # 辺で結ばれている頂点の集合
    result = []  # 各クエリの結果を格納するリスト

    for query in queries:
        if query[0] == 1:  # クエリの種類が1の場合
            u, v = query[1]-1, query[2]-1
            edges[u].add(v)
            edges[v].add(u)# 辺を追加
            connected.add(u)  # uとvを結ぶ辺があるのでuをconnectedに追加
            connected.add(v)  # uとvを結ぶ辺があるのでvをconnectedに追加

        elif query[0] == 2:  # クエリの種類が2の場合
            v = query[1]-1
            # 辺の集合からvに関連する辺を削除
            for u in edges[v]:
                edges[u].discard(v)
                if len(edges[u])==0:
                    connected.discard(u)
            edges[v] = set()
            connected.discard(v)  # vをconnectedから削除

        # 他のどの頂点とも辺で結ばれていない頂点の数を計算
        disconnected_count = N - len(connected)
        result.append(disconnected_count)

    return result


# 入力の読み込み
N, Q = map(int, input().split())
queries = []
for _ in range(Q):
    query = list(map(int, input().split()))
    queries.append(query)

# クエリの処理と結果の出力
results = process_queries(N, queries)
for res in results:
    print(res)
