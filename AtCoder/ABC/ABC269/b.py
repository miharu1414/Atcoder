from tracemalloc import start


s = [input() for i in range(10)]

start_x,start_y,goal_x,goal_y = -1,11,-1,11

for i in range(10):
    for j in range(10):
        if start_x == -1 and s[i][j] == '#':
            start_x = i+1
        if start_y == 11 and s[i][j] == '#':
            start_y = j+1

for i in range(10):
    for j in range(10):
        if goal_x == -1 and s[9-i][9-j] == '#':
            goal_x = 10-i
        if goal_y == 11 and s[9-i][9-j] == '#':
            goal_y = 10-j

print(start_x,goal_x)
print(start_y,goal_y)