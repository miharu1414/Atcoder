# https://atcoder.jp/contests/abc249/tasks/abc249_d
n = int(input())
a = list(map(int,input().split()))
num = [0]*200001
max_a = -1
for i in range(n):
    num[a[i]]+=1
    max_a = max(max_a,a[i])
ans =0 
for i in range(1,len(num)+1):
    for j in range(1,max_a//i+1):
        if i*j > len(num):
            break
        ans += num[i] * num[j] * num[i*j]
print(ans)