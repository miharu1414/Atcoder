# https://atcoder.jp/contests/typical90/tasks/typical90_bw
n = int(input())
import collections

def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a
c = collections.Counter(prime_factorize(n))

import math
    
sum = sum(list(c.values()))

print(math.ceil(math.log2(sum)))
