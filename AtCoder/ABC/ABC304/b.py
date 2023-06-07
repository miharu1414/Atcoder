n = int(input())

keta = len(str(n))

ans = ""
for i in range(len(str(n))):
    if i < 3:
        ans = ans + str(n)[i]
    else:
        ans += "0"
print(ans)
    