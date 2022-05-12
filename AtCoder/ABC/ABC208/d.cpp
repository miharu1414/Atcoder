#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using pii = pair<int, int>;
using Pll = pair<long long, long long>;
using vec = vector<int>;
using vecll = vector<long long>;
using mat = vector<vector<int>>;
using matll = vector<vector<long long>>;
#define rep(i, n) for(int i = 0; i < (int)(n); i++)
#define all(v) v.begin(), v.end()
#define endl "\n"
#define _GLIBCXX_DEBUG
#define absolute(a) max(a, -a)

constexpr int MOD = 1000000007;
const int INF = 1 << 30;

template <typename T> T gcd(T a, T b) { return b ? gcd(b, a % b) : a; }
template <typename T> T lcm(T a, T b) { return a / gcd(a, b) * b; }

int main() {
int n,m;
cin>>n>>m;
vector<vector<ll>> dp(n,vector<ll> (n,INF));
for(int i =0;i<m;i++){
    int a,b,c;
    cin>>a>>b>>c;
    dp[a][b]=c;
    dp[a][a]=0;
    dp[b][b]=0;
}
ll ans =0;
    for (int k = 0; k < n; k++){       // 経由する頂点
        for (int i = 0; i < n; i++) {    // 始点
            for (int j = 0; j < n; j++) {  // 終点
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j]);
                if(dp[i][j]!=INF){
                    ans += dp[i][j];
                }
      }
    }
  }
cout<<ans<<endl;


}
