H, W = map(int, input().split())

def check_sequence(row, col, direction):
    word = 'snuke'
    for i in range(5):
        if direction == 'vertical':
            if grid[row + i][col] != word[i]:
                return False
        elif direction == 'horizontal':
            if grid[row][col + i] != word[i]:
                return False
        elif direction == 'diagonal':
            if grid[row + i][col + i] != word[i]:
                return False
            
        elif direction == 'diagonal1':
            if grid[row - i][col + i] != word[i]:
                return False
    return True

def check_sequence1(row, col, direction):

    word1 = 'ekuns'
    for i in range(5):
        if direction == 'vertical':
            if grid[row + i][col] != word1[i]:
                return False
        elif direction == 'horizontal':
            if grid[row][col + i] != word1[i]:
                return False
        elif direction == 'diagonal':
            if grid[row + i][col + i] != word1[i]:
                return False
        elif direction == 'diagonal1':
            if grid[row - i][col + i] != word1[i]:
                return False
    return True
grid = []
for _ in range(H):
    grid.append(input())

for i in range(H):
    for j in range(W):
        if i + 4 < H and check_sequence(i, j, 'vertical'):
            print(i + 1, j + 1)
            print(i + 2, j + 1)
            print(i + 3, j + 1)
            print(i + 4, j + 1)
            print(i + 5, j + 1)
            exit()
        if j + 4 < W and check_sequence(i, j, 'horizontal'):
            print(i + 1, j + 1)
            print(i + 1, j + 2)
            print(i + 1, j + 3)
            print(i + 1, j + 4)
            print(i + 1, j + 5)
            exit()
        if i + 4 < H and j + 4 < W and check_sequence(i, j, 'diagonal'):
            print(i + 1, j + 1)
            print(i + 2, j + 2)
            print(i + 3, j + 3)
            print(i + 4, j + 4)
            print(i + 5, j + 5)
            exit()
            
        if i - 4 >= 0 and j + 4 < W and check_sequence(i, j, 'diagonal1'):
            print(i +1,  j + 1)
            print(i , j + 2)
            print(i - 1 , j + 3)
            print(i - 2, j + 4)
            print(i - 3, j + 5)
            exit()
        if i + 4 < H and check_sequence1(i, j, 'vertical'):
            print(i + 5, j + 1)
            print(i + 4, j + 1)
            print(i + 3, j + 1)
            print(i + 2, j + 1)
            print(i + 1, j + 1)


            exit()
        if j + 4 < W and check_sequence1(i, j, 'horizontal'):
            print(i + 1, j + 5)
            print(i + 1, j + 4)
            print(i + 1, j + 3)
            print(i + 1, j + 2)
            print(i + 1, j + 1)
            exit()
        if i + 4 < H and j + 4 < W and check_sequence1(i, j, 'diagonal'):
            print(i + 5, j + 5)
            print(i + 4, j + 4)
            print(i + 3, j + 3)
            print(i + 2, j + 2)
            print(i + 1, j + 1)
            exit()
            
        if i - 4 >= 0 and j + 4 < W and check_sequence1(i, j, 'diagonal1'):
            print(i - 3, j + 5)
            print(i - 2, j + 4)
            print(i - 1 , j + 3)
            print(i , j + 2)
            print(i +1,  j + 1)



            exit()