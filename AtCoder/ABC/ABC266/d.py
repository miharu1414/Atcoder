from hashlib import new
from re import L

#####segfunc#####
def segfunc(x, y):
    return max(x, y)
#################

#####ide_ele#####
ide_ele = -float('inf')
#################

class SegTree:
    """
    init(init_val, ide_ele): 配列init_valで初期化 O(N)
    update(k, x): k番目の値をxに更新 O(logN)
    query(l, r): 区間[l, r)をsegfuncしたものを返す O(logN)
    """
    def __init__(self, init_val, segfunc, ide_ele):
        """
        init_val: 配列の初期値
        segfunc: 区間にしたい操作
        ide_ele: 単位元
        n: 要素数
        num: n以上の最小の2のべき乗
        tree: セグメント木(1-index)
        """
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.tree = [ide_ele] * 2 * self.num
        # 配列の値を葉にセット
        for i in range(n):
            self.tree[self.num + i] = init_val[i]
        # 構築していく
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, k, x):
        """
        k番目の値をxに更新
        k: index(0-index)
        x: update value
        """
        k += self.num
        self.tree[k] = x
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def query(self, l, r):
        """
        [l, r)のsegfuncしたものを得る
        l: index(0-index)
        r: index(0-index)
        """
        res = self.ide_ele

        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.tree[l])
                l += 1
            if r & 1:
                res = self.segfunc(res, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return res


n = int(input())
T,X,A = [],[],[]
for i in range(n):
    t,x,a = map(int,input().split())
    T.append(t)
    X.append(x)
    A.append(a)




a = [0,0,0,0,0]
seg = SegTree(a, segfunc, ide_ele)

before_t = 0

for i in range(n):
    dif_t = T[i] - before_t
    before_t = T[i]

    new_seg = []
    for j in range(5):
        ans = 0
        left = max(0,j-dif_t)
        right = min(5,j+dif_t+1)
        if T[i]<j:
            ans = 0
        elif X[i] == j :
            ans += seg.query(left,right) + A[i]
        else:
            ans += seg.query(left,right)
        new_seg.append(ans)

    # セグメント木の更新
    for k in range(5):
        seg.update(k,new_seg[k])
print(seg.query(0,5))








