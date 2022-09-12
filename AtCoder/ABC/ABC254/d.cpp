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
    int n;
    cin>>n;
    vector<bool> sq(n+1,false);
    vector<vector<int>> d(n+1);
    for(int i = 1;i*i<=n;i++)sq[i*i] = true;
    for(int i =1;i<=n;i++){
        for(int j = i; j<=n;j+=i){
            d[j].push_back(i);
        }
    }
    vector<int> cnt(n+1);
    for(int i = 1;i<=n;i++){
        int f = 0;
        for(int j = 0;j<d[i].size();j++) if(sq[d[i][j]]) f = d[i][j];
        cnt[i/f]++;
    }
    int ans = 0;
    rep(i,n) ans += cnt[i+1]*cnt[i+1];
    cout<<ans<<endl; 

}