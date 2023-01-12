x, n = map(int,input().split())
p = list(map(int,input().split()))

li = [i for i in range(-1,103)]
p_set = set(p)
new_array = []
for i in range(len(li)):
    if li[i] not in p_set:
        new_array.append(li[i])

import bisect
ans = bisect.bisect_right(new_array,x)
last = ans -1
if abs(new_array[last] - x) > abs(new_array[last+1]-x):
    last += 1
print(new_array[last])