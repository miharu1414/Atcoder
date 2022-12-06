"""nを素因数分解"""
"""2以上の整数n => [[素因数, 指数], ...]の2次元リスト"""

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr



n = int(input())
a = list(map(int,input().split()))
b = []
nc = 0
for i in range(n):
    if a[i] != 1:
        b.append(a[i])
        nc += 1
n = nc
if nc == 0:
    print("pairwise coprime")
    exit()
pos = [0]*1000001

ok_pair = 1
for i in range(n):
    li= factorization(a[i])
    for j in range(len(li)):
         pos[li[j][0]] += 1
         if pos[li[j][0]] > 1:
             ok_pair =0
             break
    if ok_pair == 0:
        break
if ok_pair:
    print("pairwise coprime")
    exit()

gcd = a[0]
import math
for i in range(1,n):
    gcd = math.gcd(gcd,a[i])
if gcd == 1:
    print("setwise coprime") 
    exit()
print("not coprime")