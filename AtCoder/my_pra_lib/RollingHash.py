# https://kyoroid.github.io/algorithm/string/rolling_hash.html

class RollingHash():
    """ローリングハッシュのpython用のライブラリ"""
    def __init__(self, S, b = 3491, mod = 999999937):
        """任意の基数と法でハッシュを生成する  基数と法は互いに素でなければならない"""
        n = len(S)
        self.prefix = prefix = [0] * (n+1)
        self.power = power = [1] * (n+1)
        self.b = b
        self.m = mod
        for i in range(n):
            c = ord(S[i])
            prefix[i+1] = (prefix[i] * b + c) % mod
            power[i+1] = (power[i] * b) % mod
    
    def get_hash(self, l , r):
        """S[l, r) のハッシュを求める"""
        return (self.prefix[r] - self.power[r-l] * self.prefix[l]) % self.m

    def concat(self, h1, h2, l2):
        """S1+S2 のハッシュを、それぞれのハッシュから求める"""
        return (self.power[l2] * h1 + h2) % self.m

    def lcp(self, l1, r1, l2, r2):
        """S[l1, r1) とS[l2, r2) の最大共通接頭辞を求める"""
        # LCPの最小値 (範囲内)
        low = 0
        # LCPの最大値 + 1 (範囲外)
        high = min(r1-l1, r2-l2) + 1
        while high - low > 1:
            mid = (high + low) // 2
            if self.get(l1, l1 + mid) == self.get(l2, l2 + mid):
                low = mid
            else:
                high = mid
        return low








"""
from pprint import pprint
from collections import defaultdict

S = "mississippi"
N = len(S)
# 長さ3の文字列を検索
size = 3

rh = RollingHash(S, m=2019, b=10**9+7)

d = defaultdict(list)
for i in range(N-size+1):
    h = rh.get(i, i+size)
    d[h].append(i)
pprint(d)
"""