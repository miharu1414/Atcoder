S = input()

# 条件1の判定
b_indices = [i for i, c in enumerate(S) if c == "B"]
if len(b_indices) == 2 and b_indices[0] % 2 != b_indices[1] % 2:
    pass
else:
    print("No")
    exit()

# 条件2の判定
r_indices = [i for i, c in enumerate(S) if c == "R"]
if len(r_indices) == 2 and r_indices[0] < r_indices[1]:
    k_index = S.find("K")
    if r_indices[0] < k_index < r_indices[1]:
        pass
    else:
        print("No")
        exit()
else:
    print("No")
    exit()

print("Yes")