n = int(input())

alpha = [chr(i+ord('a')) for i in range(26)]
alpha = ['z']+alpha[:]
S = ""
while n>0:
    if n % 26==0:
        S += 'z'
        n = n//26 -1
    else:
        S += alpha[n%26]
        n//=26
new_str = ''.join(list(reversed(S)))
print(new_str)