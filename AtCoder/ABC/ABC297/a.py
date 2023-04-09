N, D = map(int, input().split())
T = list(map(int, input().split()))

double_click_time = -1  # ダブルクリックが成立する最初の時刻

for i in range(1, N):
    if T[i] - T[i-1] <= D:
        double_click_time = T[i]
        break

print(double_click_time)