from re import L


n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))

cnt = 0

num_a = [0]*(n+1)
num_b = [0]*(n+1)
num_c = [0]*(n+1)
for i in range(n):
    num_a[a[i]]+=1
    num_c[b[c[i]-1]]+=1
    

for i in range(n+1):
    cnt += num_a[i]*num_c[i]
print(cnt)