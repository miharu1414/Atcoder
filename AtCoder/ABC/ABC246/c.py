n,k,x = map(int,input().split( ))
a = list(map(int,input().split()))
a.sort(reverse=True)
for i in range(n):
    if k == 0:
        break
    use =int(a[i] / x)
    if use > k:
        use = k
    a[i] -= x*use
    k-= use

a.sort(reverse = True)
for i in range(k):
    if i >= n:
        break
    a[i] = 0
ans = sum(a)
print(ans)    