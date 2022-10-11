n = input()
if int(n) >=42:
    n = str(int(n)+1)
ans = "AGC"
for i in range(3-len(n)):
    ans+='0'
ans += n
print(ans)