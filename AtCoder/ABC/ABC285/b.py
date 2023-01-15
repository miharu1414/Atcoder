n = int(input())
s = input()

ans = [0]*(n)
for i in range(1,n):
    ans[i] = n-i
for i in range(1,n):
    flag = n-1
    for k in range(n-i):
        if s[k] == s[k+i]:
            ans[i] = k
            break
    print(ans[i])
