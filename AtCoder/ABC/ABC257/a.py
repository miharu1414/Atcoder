n,x = map(int,input().split())
S = ""
for i in range(26):
    for j in range(n):
        S += chr(i+65)
print(S[x-1])