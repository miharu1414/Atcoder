n = int(input())
if n < 8:
    print(0)
    exit()

from bisect import bisect, bisect_right
import math

def sieve_eratosthenes(n = 1000000):
    primes = [0, 1] * (n // 2 + 1)
    if n % 2 == 0:
        primes.pop()
    primes[1] = 0
    primes[2] = 1
    for p in range(3, int(n ** 0.5) + 1, 2):
        if primes[p]:
            for q in range(p * p, n + 1, 2 * p):
                primes[q] = 0
    return primes
sosuu_01 = sieve_eratosthenes()
sosuu = []
for i in range(len(sosuu_01)):
    if sosuu_01[i] ==1:
        sosuu.append(i)
ans = 0
pair = 1
while 1:
    if sosuu[pair]**3 > 2*n:
        break
    pos = bisect_right(sosuu[:pair], n//sosuu[pair]**3)

    ans += pos
    pair +=1
print(ans)