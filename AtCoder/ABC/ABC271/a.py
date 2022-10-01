n = int(input())
ans = hex(n)

A = ""
s =str(ans).upper()
for i in range(len(s)):
    if s[i] !='X':
        A += s[i]
if len(A) == 1:
    an = '0'+A
else:
    an = ''
    for i in range(2):
        an+=A[len(A)+i-2]
print(an)