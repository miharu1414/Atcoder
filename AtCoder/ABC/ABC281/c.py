n,t = map(int,input().split())
a = list(map(int,input().split()))
Sum = sum(a)
left = t  % Sum 
for i in range(n):
    if left <= a[i]:
        print(i+1,left)
        exit()
    else:
        left -= a[i]
    