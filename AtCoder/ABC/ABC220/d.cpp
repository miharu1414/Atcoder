#include <bits/stdc++.h> 
#include <atcoder/all>    
using namespace std;
using namespace atcoder;
using ll = long long;
using pii = pair<int, int>;
using pll = pair<long long,long long>;
using vec = vector<int>;
using vecll = vector<long long>;
using mat = vector<vector<int>>;
using matll = vector<vector<long long>>;
#define rep(i, n) for(int i = 0; i < (int)(n); i++)
#define all(v) v.begin(), v.end()
#define endl "\n"
#define _GLIBCXX_DEBUG
constexpr int MOD = 1000000007;
const int INF = 1 << 30;
template<typename T> T gcd(T a, T b) { return b ? gcd(b, a%b) : a; }
template<typename T> T lcm(T a, T b) { return a / gcd(a, b) * b ;}

using mint = modint998244353;


    int main(){
        int n;cin>>n;
        vector<int> a(n);
        rep(i,n) cin>>a[i];
        mint dp[n][10];
        memset(dp,0,sizeof(dp));
        dp[0][a[0]] = 1;
        rep(i,n-1){
            rep(j,10){
                dp[i+1][(j*a[i+1])%10] += dp[i][j];
                dp[i+1][(j+a[i+1])%10] += dp[i][j];
            }
        }
        rep(i,10) cout<<dp[n-1][i].val()<<endl;
    }