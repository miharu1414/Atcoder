n = int(input())
ans_s = dict()
s = [input() for i in range(n)]
ans_s['AC'] = 0
ans_s['WA'] = 1
ans_s['TLE'] = 2
ans_s['RE'] = 3
num = [0]*4
for i in range(n):
    num[ans_s[s[i]]] += 1
print(f'AC x {num[0]}')
print(f'WA x {num[1]}')
print(f'TLE x {num[2]}')
print(f'RE x {num[3]}')