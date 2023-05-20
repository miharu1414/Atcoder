a, b = map(int,input().split())

ans = a//b
amari = a%b
if amari:
    ans += 1
print(ans)