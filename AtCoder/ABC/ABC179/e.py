n, x, m = map(int,input().split())


num = [0]*100001

roop = []
roop_set = set()
for i in range(n):
    num[x] += 1
    x = (x * x) %m
    if x == 0:
        break
    if x in roop_set:
        for j in range(n):
            if roop[j] == x:
                memo = j
                break
        left = n-i-1
        kaisuu = left//(i-j)
        amari = left%(i-j)
        for k in range(j,i):
            num[roop[k]]+=kaisuu
        for k in range(amari):
            num[roop[j+k]]+=1
        break
    else:
        roop.append(x)
        roop_set.add(x)
        continue


ans = 0
for i in range(len(num)):
    ans += i*num[i]
print(ans)
    