import decimal
n = int(input("人数："))
p = float(input("1が出る確率:"))
dp = [[1.0-p,p] for i in range(n)]

for i in range(1,n):
    dp[i][0] = dp[i-1][1]*(1.0-p)*0.5
    dp[i][1] = dp[i-1][0]*p*0.5
for i in range(n):
    decimal.getcontext().prec = 7
    P_i0 = decimal.Decimal(dp[i][0])*100
    P_i1 = decimal.Decimal(dp[i][1])*100
    Sum = P_i0 + P_i1
    print(f"{i+1}人目で")
    # print(f"0と回答した時にカスケードが起きない確率:",'{:.5g}'.format(P_i0),'%')
    # print(f"1と回答した時にカスケードが起きない確率:",'{:.5g}'.format(P_i1),'%')
    print(f"カスケードが起きない確率：",'{:.4g}'.format(Sum),'%')
    
    
    