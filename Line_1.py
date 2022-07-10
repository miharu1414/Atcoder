import sys


# 各頂点iについて深さ優先探索　－＞　間に合わない
    #モチベーション： 一度計算した情報を格納して利用したい　メモ化？
    # 部屋iから距離1で移動できる部屋どうしは必ず2回以内で移動できる




def main(n,p):

    # 部屋の関係性をグラフ（配列）に格納する
    Graph = [[] for i in range(n+2)]
    for i in range(n-1):
        Graph[i+2].append(p[i])
        Graph[p[i]].append(i+2)


    answer = []

    room = [[] for _ in range(n+1)]


    # 始点をiとして深さ優先探索を行う
    for i in range(1,n+1):
        nodes = [[]for j in range(4)]
        dist = [-1] * (n+1)

        # 部屋iを始点とする
        dist[i] = 0
        nodes[0] = [i]
        # 部屋iから3回以内で移動可能な部屋
        possible_room = [i]

        # k回目の移動で部屋iからたどり着く部屋を探索
        for k in range(1,4):
            # k-1回目でたどり着いた部屋vから移動
            for v in nodes[k - 1]:
                # 部屋v と連結している部屋next_vを探索
                for next_v in Graph[v]:
                    # 部屋next_vが探索済みならなにもしない
                    if dist[next_v] != -1:
                        continue

                    dist[next_v] = dist[v]+1
                    nodes[k].append(next_v)
                    possible_room.append(next_v)
        # print(*possible_room)
        # print(len(possible_room))

        # 答えの配列answerに部屋iから3回以内に移動できる部屋の数を追加する　
        answer.append(len(possible_room))
    
    print(*answer)




def big(n,p):

    # 部屋の関係性をグラフ（配列）に格納する
    Graph = [[] for i in range(n+2)]
    for i in range(n-1):
        Graph[i+2].append(p[i])
        Graph[p[i]].append(i+2)

 
    answer = []

    room = [[] for _ in range(n+1)]


    # 始点をiとして深さ優先探索を行う
    for i in range(1,n+1):
        nodes = [[]for j in range(4)]
        dist = [-1] * (n+1)

        # 部屋iを始点とする
        dist[i] = 0
        nodes[0] = [i]
        # 部屋iから3回以内で移動可能な部屋
        possible_room = [i]

        # k回目の移動で部屋iからたどり着く部屋を探索
        for k in range(1,4):
            # k-1回目でたどり着いた部屋vから移動
            for v in nodes[k - 1]:
                # 部屋v と連結している部屋next_vを探索
                for next_v in Graph[v]:
                    # 部屋next_vが探索済みならなにもしない
                    if dist[next_v] != -1:
                        continue

                    dist[next_v] = dist[v]+1
                    nodes[k].append(next_v)
                    possible_room.append(next_v)
        # print(*possible_room)
        # print(len(possible_room))

        # 答えの配列answerに部屋iから3回以内に移動できる部屋の数を追加する　
        answer.append(len(possible_room))
    
    print(*answer)


if __name__ == '__main__':
    n = int(input())
    p = list(map(int,input().split()))
    if n <= 100000:
        main(n,p)
    else:
        big(n,p)
