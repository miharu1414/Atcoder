s = input()
t = input()

ans = [[0]*(len(t)+1) for i in range(len(s)+1)]

for i in range(len(s)):
    for j in range(len(t)):
        if s[i] == t[j]:
            ans[i+1][j+1] = ans[i][j] + 1
        else:
            if ans[i+1][j]>=ans[i][j] and ans[i+1][j]>=ans[i][j+1]:
            
                ans[i+1][j+1] = ans[i+1][j]
            elif ans[i][j]>=ans[i+1][j] and ans[i][j]>=ans[i][j+1]:
                ans[i+1][j+1] = ans[i][j]
            
            elif ans[i][j+1]>=ans[i+1][j] and ans[i][j+1] >= ans[i][j]:
                ans[i+1][j+1]  = ans[i][j+1]

string = ''
bef_j = 0
before = len(t)
for i in range(len(s),0,-1):
    for j in range(before,0,-1):
        if ans[i][j] == ans[i-1][j-1] + 1 and  ans[i][j] == ans[i-1][j] + 1 and  ans[i][j] == ans[i][j-1]+1:
            string += s[i-1]
            before = j-1
            break
print(string[::-1])