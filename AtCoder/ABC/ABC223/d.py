import heapq
class MultiSet:
    """多重集合

    重複する整数の集合を保持する

    """
    def __init__(self):
        self.cnt_dict = {}
        self.rank_min = []
        self.rank_max = []

    def add(self, num):
        """要素を1つ追加する

        個数辞書の更新
        昇順順位、降順順位の更新
        Args:
            num (int): 追加要素
        """
        cnt = self.cnt_dict.get(num, 0)
        self.cnt_dict[num] = cnt + 1

        heapq.heappush(self.rank_min, num)
        heapq.heappush(self.rank_max, -num)

    def erase(self, num, d):
        """要素の削除

        集合から指定要素を指定個数消す。
        順位の更新をする。

        Args:
            num (int): 削除要素
            d (int): 指定個数

        """
        cnt = self.cnt_dict.get(num, 0)
        self.cnt_dict[num] = max(0, cnt - d)
    
    def get_max(self):
        while self.cnt_dict[-self.rank_max[0]] == 0:
            -heapq.heappop(self.rank_max)
        return -self.rank_max[0]

    def get_min(self):
        while self.cnt_dict[self.rank_min[0]] == 0:
            heapq.heappop(self.rank_min)
        return self.rank_min[0]

n,m = map(int,input().split())
ab = [map(int,input().split()) for i in range(m)]
a,b = [list(i) for i in zip(*ab)]

Graph = [[] for i in range(2*10**5+1)]
num = [0]*(2*10**5+1)
for i in range(m):
    Graph[a[i]-1].append(b[i]-1)
    num[b[i]-1]+=1


mul = MultiSet()

cnt = 0
for i in range(n):
    if num[i] == 0:
        mul.add(i)
        cnt += 1

ans = []

for i in range(n):
    if cnt==0:
        break
    min = mul.get_min()
    ans.append(min)
    mul.erase(min,1)
    cnt -= 1
    for x in Graph[min]:
        num[x] -= 1
        if num[x] == 0:
            mul.add(x)
            cnt += 1
if len(ans) != n:
    print(-1)
else:
    for i in range(n):
        ans[i] += 1
    print(*ans)