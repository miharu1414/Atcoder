x = input()
n = int(input())
s = [input() for i in range(n)]

X_num = [0]*200
for i in range(len(x)):
    X_num[ord(x[i])] = i+1
weight = []
maxl = 0
for i in range(n):
    maxl = max(maxl,len(s[i]))
for i in range(n):
    cnt = 0
    for j in range(len(s[i])):
        cnt += X_num[ord(s[i][j])]
        cnt*=27
        
    for j in range(maxl - len(s[i])):
        cnt*=27
        
    weight.append([cnt,i])
weight.sort()
for i in range(n):
    print(s[weight[i][1]])