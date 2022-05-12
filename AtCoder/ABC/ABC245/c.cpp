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
    int n,k;
    cin>>n>>k;
    mat a(n,vector<int> (2)), dp(n,vector<int> (2));
    rep(i,n){
        cin>>a[i][0];
        dp[i][0] = dp[i][1] = 0;
    }
    rep(i,n) cin>>a[i][1];
    dp[0][0] = dp[0][1] = 1;

    rep(i,n-1){
        
             rep(l,2){
                if(dp[i][l]==1){
                    int dif1 = abs(a[i+1][0]-a[i][l]);
                    
                    if (dif1<=k) {
                        dp[i+1][0] = 1;
                 
                    }
                    int dif2 = abs(a[i+1][1]-a[i][l]);
               
                    if (dif2<=k){
                        dp[i+1][1] = 1;
                    }
                }
             }
    }

    if(dp[n-1][0] + dp[n-1][1] >=1) cout<<"Yes"<<endl;
    else cout<<"No"<<endl;
}