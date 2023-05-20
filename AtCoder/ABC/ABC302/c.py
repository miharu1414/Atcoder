
from itertools import permutations

def check_condition(words):
    for i in range(len(words) - 1):
        count_diff = sum(a != b for a, b in zip(words[i], words[i+1]))
        if count_diff > 1:
            return False
    return True

N, M = map(int, input().split())
S = [input() for _ in range(N)]

# 全ての並び替えパターンを生成し、条件を満たすか判定する
permutations = permutations(S)
for perm in permutations:
    if check_condition(perm):
        print("Yes")
        exit()

print("No")
