#include <bits/stdc++.h>
#include <atcoder/modint>
using namespace std;
using mint = atcoder::modint998244353;
int main() {
	int n,p;
	cin>>n>>p;
  vector<mint> dp(n + 1, mint(0));
  mint m_inv = mint(p) / mint(100) ;
	mint m_inv2 = 1 - m_inv ;

	dp[0] = 0;
  for(int i = 1; i<=n;i++){
    dp[i] = dp[i-1]*m_inv2 + dp[max(0,i-2)] * m_inv + 1;
  }
  cout << dp[n].val() << endl;
}
