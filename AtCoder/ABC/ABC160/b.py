ans = 0
x = int(input())
ans += (x //500)*1000
x %= 500
ans += (x//5)*5
print(ans)