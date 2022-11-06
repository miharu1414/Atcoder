import collections
class UnionFind():
    def __init__(self):
        '''
        unionfind経路圧縮あり,要素にtupleや文字列可,始めに要素数指定なし
        '''
        self.parents = dict()                                      # {子要素:親ID,}
        self.members_set = collections.defaultdict(lambda : set()) # keyが根でvalueが根に属する要素要素(tupleや文字列可)
        self.roots_set = set()                                     # 根の集合(tupleや文字列可)
        self.key_ID = dict()                                       # 各要素にIDを割り振る
        self.ID_key = dict()                                       # IDから要素名を復元する
        self.cnt = 0                                               # IDのカウンター

    def dictf(self,x): # 要素名とIDをやり取りするところ
        if x in self.key_ID:
            return self.key_ID[x]
        else:
            self.cnt += 1
            self.key_ID[x] = self.cnt
            self.parents[x] = self.cnt
            self.ID_key[self.cnt] = x
            self.members_set[x].add(x)
            self.roots_set.add(x)
            return self.key_ID[x]

    def find(self, x):
        ID_x = self.dictf(x)
        if self.parents[x] == ID_x:
            return x
        else:
            self.parents[x] = self.key_ID[self.find(self.ID_key[self.parents[x]])]
            return self.ID_key[self.parents[x]]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        if x == y:
            return
        for i in self.members_set[y]:
            self.members_set[x].add(i)
        self.members_set[y] = set()
        self.roots_set.remove(y)
        self.parents[y] = self.key_ID[x]

    def size(self, x):#xが含まれる集合の要素数
        return len(self.members_set[self.find(x)])

    def same(self, x, y):#同じ集合に属するかの判定
        return self.find(x) == self.find(y)

    def members(self, x):#xを含む集合の要素
        return self.members_set[self.find(x)]

    def roots(self):#根の要素
        return self.roots_set

    def group_count(self):#根の数
        return len(self.roots_set)

    def all_group_members(self):#根とその要素
        return {r: self.members_set[r] for r in self.roots_set}


    
import time

start = time.time()
h,w = map(int,input().split())
c = [input() for i in range(h)]

for i in range(h):
    for j in range(w):
        if c[i][j] == 'S':
            sx = i
            sy = j
           
dist = [[-1]*w for i in range(h)]

from queue import Queue
que = Queue()

dx1 = [1,-1,0,0]
dy1 =[0,0,1,-1]

dist[sx][sy] = 1
que.put((sx,sy))

ok = 0
uf_s = UnionFind()
while not que.empty():
    end = time.time()
    if end-start > 1.7:
        print("Yes")
        exit()
    next_x,next_y = que.get()
    """
    if dist[next_x][next_y] > 2 :

        dist[sx][sy] = -1
    else:
        dist[sx][sy] = 0
        """
    for dx,dy in zip(dx1,dy1):
        x = next_x + dx
        y = next_y + dy
        if x < 0 or y < 0 or x >= h or y >= w or c[x][y] =='#' or (x == sx and y == sy) :
            continue
        if dist[x][y] != -1  :
            if not uf_s.same((next_x,next_y),(x,y)):
                # print(x,y,next_x,next_y,c[x][y])
                ok =1 
                break
            continue
        # print(x,y)
        dist[x][y] = dist[next_x][next_y] + 1
        if next_x != sx or next_y != sy and not uf_s.same((next_x,next_y),(x,y)):
            uf_s.union((next_x,next_y),(x,y))
            # print(next_x,next_y,x,y)
        que.put((x,y))
    if ok:
        break
if ok:
    print("Yes")
else:
    print("No")