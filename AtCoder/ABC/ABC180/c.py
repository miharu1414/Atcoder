n = int(input())
i = 1

ans = set()
while i*i<=n:
    if n % i == 0:
        ans.add(i)
        ans.add(n//i)
    i+=1
A = list(ans)
A.sort()
for a in A:
    print(a)