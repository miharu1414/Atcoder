s = [input() for i in range(9)]
ans = 0
set_ans = set()
for i in range(9):

    for j in range(9):

        if s[i][j] == '#':
            
            for k in range(9):
                for l in range(9):

                    if i == k and j == l:
                        break
                    if s[k][l] == '#':
                        dif_x = i - k
                        dif_y = j - l
                        
                        nx1 = i + dif_y
                        ny1 = j - dif_x
                        nx2 = k + dif_y
                        ny2 = l - dif_x
                        
                        if nx1 < 0 or nx1 > 8 or ny1 < 0 or ny1 > 8 or nx2 < 0 or nx2 > 8 or ny2 < 0 or ny2 >8:
                            continue
                        if s[nx1][ny1] == '#' and s[nx2][ny2] == '#':
                            ans += 1
                            Ans = set()
                            Ans.add((i,j))
                            Ans.add((k,l))
                            Ans.add((nx1,ny1))
                            Ans.add((nx2,ny2))

                            set_ans.add(frozenset(Ans))
print(len(set_ans))
                            
