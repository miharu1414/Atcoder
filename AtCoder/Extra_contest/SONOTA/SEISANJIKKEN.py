print("発注余力をコピペして")
yoryoku = [int(input()) for i in range(10)]
ans = [0]*10
now = []


for i in range(10):
    now.append([yoryoku[i],i])
add = [0]*10
n = int(input("追加する数量を入力して"))
for i in range(n):
    now.sort(reverse=True)
    now[0][0] -= 1
    add[now[0][1]] += 1

now = sorted(now,  key=lambda x: x[1])
print("番号　振り分け後の発注余力　追加量",)
for i in range(10):
     print(now[i][1]+1,now[i][0],add[i])
     
            
            
    
    