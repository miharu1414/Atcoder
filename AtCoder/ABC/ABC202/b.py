s = input()

T = {"0":"0","1":"1","6":"9","9":"6","8":"8"}
ans = ""
for i in s[::-1]:
    ans += T[i]
print(ans)