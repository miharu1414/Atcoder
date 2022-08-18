s = input()
alpha = []
for i in range(3):
    alpha.append(s[i])
import collections 
c = collections.Counter(alpha)
num = len(c.keys())
if num == 3:
    print(6)
elif num == 2:
    print(3)
else:
    print(1)