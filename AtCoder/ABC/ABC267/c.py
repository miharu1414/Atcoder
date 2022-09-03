n,m = map(int,input().split())
a = list(map(int,input().split()))
sum = [0]*(n+1)
for i in range(1,n+1):
    sum[i] = sum[i-1] + a[i-1]

W_sum = [0]*(n-m+1)
for i in range(m):
    W_sum[0] += (i+1)*a[i]
for i in range(1,n+1-m):
    W_sum[i] = W_sum[i-1] - (sum[m+i-1]-sum[i-1]) + m * a[i+m-1]
print(max(W_sum))
    
