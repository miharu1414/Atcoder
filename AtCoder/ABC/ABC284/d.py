# 1 以上 N 以下の整数が素数かどうかを返す
def Eratosthenes(N):
    # テーブル
    isprime = [True] * (N+1)

    # 0, 1 は予めふるい落としておく
    isprime[0], isprime[1] = False, False

    # ふるい
    for p in range(2, N+1):
        # すでに合成数であるものはスキップする
        if not isprime[p]:
            continue

        # p 以外の p の倍数から素数ラベルを剥奪
        q = p * 2
        while q <= N:
            isprime[q] = False
            q += p

    # 1 以上 N 以下の整数が素数かどうか
    return isprime


# python
# 補助関数
def suspect(a, t, n):
    x = pow(a, t, n)
    n1 = n - 1
    while t != n1 and x != 1 and x != n1:
        x = pow(x, 2, n)
        t <<= 1
    return t & 1 or x == n1
 
# メイン
# 2^64までの決定的アルゴリズムとして実装しているので、ランダム要素は無い
# ランダムとして用いる場合は、check_listにランダム抽出された数を採用し、20～50個程度試す
import random
def miller_rabin(n):
    if n == 2: return True
    if n == 1 or n & 1 == 0: return False

    d = (n - 1) >> 1
    while d & 1 == 0:
        d >>= 1

    for k in range(100):
        a = random.randint(1, n - 1)
        t = d
        y = pow(a, t, n)

        while t != n - 1 and y != 1 and y != n - 1:
            y = (y * y) % n
            t <<= 1

        if y != n - 1 and t & 1 == 0:
            return False

    return True



# 50 以下の素数をすべて求める
kazu = 10**7+1
isprime = Eratosthenes(kazu)
sosuu = []
issouu = set()
for i in range(kazu):
    if isprime[i]==1:
        sosuu.append(i)
        issouu.add(i)
heihousuu = set()
import math
for i in sosuu:
    heihousuu.add(i*i)
t = int(input())





for _ in range(t):
    n = int(input())
    j = 0
    while 1:
        p = sosuu[j]
        if n%(p*p)==0:
            q = n//(p*p)
            if q <= kazu and q in issouu:
                print(p,q)
                break
            elif q > kazu and miller_rabin(q):
                print(p,q)
                break
        elif n%p==0:
            q = n//p
            if q in heihousuu:
                print(int(math.sqrt(q)),p)
                break
            
            
            elif q == int(math.sqrt(q))*int(math.sqrt(q)):
                q = int(math.sqrt(q))
                if q <= kazu and q in issouu:
                    print(q,p)
                    break
                elif q > kazu and miller_rabin(q):
                    print(q,p)
                    break
        j += 1