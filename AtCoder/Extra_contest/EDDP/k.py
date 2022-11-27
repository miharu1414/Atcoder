n, k = map(int,input().split())
a = list(map(int,input().split()))

K  = [0]*100001

K[0] = 0
for i in range(1,k+1):
    for j in range(n):
        if i - a[j]<0:
            break
        if i - a[j] >= 0:
            K[i] = max(K[i],abs(K[i-a[j]]-1))
if K[k] == 1:
    print("First")
else:
    print("Second")
        