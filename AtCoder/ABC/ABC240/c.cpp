#include <bits/stdc++.h>
#include <atcoder/all>

using namespace std;
using ll = long long;
using pii = pair<int, int>;
using Pll = pair<long long, long long>;
using vec = vector<int>;
using vecll = vector<long long>;
using mat = vector<vector<int>>;
using matll = vector<vector<long long>>;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define all(v) v.begin(), v.end()
#define endl "\n"
#define _GLIBCXX_DEBUG


constexpr int MOD = 1000000007;
const long long INF = 1LL << 60;
const int inf = 1<<30;
template <typename T>
T gcd(T a, T b) { return b ? gcd(b, a % b) : a; }
template <typename T>
T lcm(T a, T b) { return a / gcd(a, b) * b; }


int main() {
    int n,x;cin>>n>>x;
    vec a(n),b(n);
    mat dp(n+1,vector<int> (x+1));
    rep(i,n+1) rep(j,x+1) dp[i][j] = 0;
    dp[0][0] =1;
    rep(i,n) cin>>a[i]>>b[i];
    for(int i = 1; i<=n;i++){
        for(int j =0;j<=x;j++){
            if(j-a[i-1]<0);
            else if (dp[i-1][j-a[i-1]]==1) dp[i][j] =1;
            if(j-b[i-1]<0);
            else if (dp[i-1][j-b[i-1]]==1) dp[i][j] =1;
        }
    }
    if(dp[n][x]==1) cout<<"Yes"<<endl;
    else cout<<"No"<<endl;

}