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
x = factorization(n)
import collections
count = 0
for i in range(len(x)):
    count += x[i][1]

i = 0
import math
if count == 1:
    print(0)
else:
    print(math.ceil(math.log2(count)))
