n,k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
count = 0
for i in range(n):
    count += abs(b[i]-a[i])
if count ==k :
    print('Yes')
elif count<k and (k-count)%2==0:
    print("Yes")
else:
    print('No')