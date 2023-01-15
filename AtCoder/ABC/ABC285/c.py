s = input()
Len = len(s)
def Junban(x):
    return ord(x) - ord('A') + 1
ans  = 0
for i in range(len(s)):
    ans += 26 ** (Len - i - 1) * Junban(s[i])
print(ans)