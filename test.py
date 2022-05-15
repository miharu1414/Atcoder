print(ord('a'))
print(ord('A'))
print(ord('b'))
alpha = [0]*100
s = input()
for i in range(len(s)):
    alpha[ord(s[i])-65]+=1
print(*alpha)