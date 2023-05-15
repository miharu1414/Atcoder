s = input()
n = int(input())
ans = ["" for i in range(len(s))]
def decimal_to_binary(n):
    """10進数の整数nを2進数の文字列に変換する"""
    if n == 0:
        return '0'
    binary = ''
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2
    return binary

nb = decimal_to_binary(n)
for i in range(len(s)-len(nb)):
    nb = "0"+nb
tiisa = 0
str_s = ""
for i in s:
    if i == '?':
        str_s = str_s + '1'
    else:
        str_s = str_s + i
decimal_num0 = int(str_s,2)
if decimal_num0 < n:
    tiisa = 1
    
    
    
str_s = ""
for i in s:
    if i == '?':
        str_s = str_s + '0'
    else:
        str_s = str_s + i
decimal_num0 = int(str_s,2)
if decimal_num0 > n:
    print(-1)
    exit()
    
nb1 = ""
for i in range(len(s)):
    nb1 = nb[len(nb) - i- 1] + nb1 

length = len(s)
idx = []
for i in range(len(s)):
    if s[i] == '?':
        idx.append(i)
        ans[i] = nb1[i]
        if tiisa:
            ans[i] = '1'
    elif s[i] == '0' and nb1[i] =='1':
        ans[i] = '0'
        tiisa = 1
    else:
        ans[i] = s[i]


ans1 = ""
for i in range(len(ans)):
    ans1 = ans1 + ans[i]

decimal_num = int(ans1, 2)
if decimal_num  > n:
    for i in idx:
        ans[i] = '0'
        ans2 = ""
        for i in range(len(ans)):
            ans2 = ans2 + ans[i]
        if ans2 <= nb:
            decimal_num = int(ans2, 2)
            print(decimal_num)
            exit()

        
if decimal_num0 < n:
    decimal_num = int(ans1, 2)
    print(decimal_num)

elif ans1 > nb:
    print(-1)
else:
    decimal_num = int(ans1, 2)
    print(decimal_num)

    