p = list(map(int,input().split()))

start = 'a'

ans = ''
for i in range(26):
    ans += chr(ord('a')+p[i]-1)
print(ans)