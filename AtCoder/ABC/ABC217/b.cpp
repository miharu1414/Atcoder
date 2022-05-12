#include <bits/stdc++.h>     
using namespace std;
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
int main(){
    vector<string> dp(3);
    rep(i, 3) cin >> dp[i];
    vector<int> ist(4,0);
    map<string, int> a;
    a["ABC"] = 0;
    a["ARC"] = 1;
    a["AGC"] = 2;
    a["AHC"] = 3;
    vector<string> b = {"ABC", "ARC", "AGC", "AHC"};
    rep(i, 3){
        ist[a[dp[i]]]++;
    }
    rep(i,4){
        if(ist[i]==0) cout << b.at(i) << endl;
    }
}