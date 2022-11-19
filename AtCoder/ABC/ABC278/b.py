h , m = map(int,input().split())

for i in range(h,24):
    for j in range(59):
        if i == h and j < m:
            continue

            
        if (i//10 == 1 or i//10 == 0) and i%10 <6:
            print(i,j)
            exit()
        if (i//10 == 2 and j//10 < 4):
            print(i,j)
            exit()
        
for i in range(h):
    for j in range(59):
      
            
        if (i//10 == 1 or i//10 == 0) and i%10 < 6:
            print(i,j)
            exit()
        if (i//10 == 2 and j//10 < 4):
            print(i,j)
            exit()  