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
    int n,q;
    cin>>n;
    vector<int> R(n),C(n);
    rep(i,n) cin>>R[i];
    rep(i,n) cin>>C[i];
    cin>>q;
    vector<int> r(q),c(q);
    rep(i,q) cin>>r[i]>>c[i];

    int score = n + 1;
    int atai;
    rep(i,q){
        atai = R[r[i]-1] + C[c[i]-1];
        if(atai>=score) cout<<'#';
        else cout<<'.';
    }
}