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


using namespace atcoder;

int mod = 998244353;
// or: typedef modint998244353 mint;

int main() {
    // print sum of array (mod 998244353)
    int n;
    cin >> n;
    vector<vector<long long>> ans(n+1,vector<long long> (10));
    vector<int> d(3);
    d[0] = -1;d[1] = 0;d[2] = 1;

    rep(i,9){
        ans[1][i+1] = 1;
        ans[2][i+1] = 3;
    }
    ans[2][1] = 2;
    ans[2][9] = 2;
    for(int i = 2;i<=n;i++){
        for(int j = 1;j<=9;j++){
            int mod_ans = 0;
            ans[i][j] =  0;
            for( auto dx : d){
                int x = j + dx;
                if (x >  9|| x<=0) continue;
                ans[i][j] += ans[i-1][x] % mod;
            }
            ans[i][j] %= mod;
        }
    }
    ll anse  =0 ;
    rep(i,9)  {
        anse += ans[n][i+1] % mod;
    }
    anse %= mod;
    cout<<anse;
}