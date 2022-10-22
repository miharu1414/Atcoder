import collections
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
a = list(map(int,input().split()))

"""
NOTE: 

・バケットを作って、0 から N-M までの値を順に引いていく
  → 毎回ソートしなくていいはず
・4sec なら N^2 の全探索でいける・・・？
  → TLE
・区間の移動ごとにO(1)の計算量で評価
"""

bkt = [0]*(n+1)
new_befa = []
befa = []



num = [0]*200001
mul = MultiSet()
for i in range(n+1):
    mul.add(i)
for i in range(n):
    if a[i] >= 0 and a[i] <= n:
        mul.erase(a[i])
        num[a[i]]+=1

    if a[i]<= n:
        befa.append([a[i],i+1])
    
new_befa = [[]for i in range(m+1)]

new_befa[0]=befa
for i in range(m):
    

    for x, y in new_befa[i]:
        new_x = x + (y)
        if x>=0 and x<=n:
            num[x]-=1
            if num[x]==0:
                mul.add(x)
        
        if new_x >= 0 and new_x <= n:
            num[new_x]+=1
            if num[new_x]==1:
                mul.erase(new_x,1)
        if new_x <= n:
            new_befa[i+1].append([new_x,y])
    
    print(mul.get_min())
        
            
        
        
        
        

        
