#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using ll = long long;
using pii = pair<int, int>;
using pll = pair<long long, long long>;
using vec = vector<int>;
using vecll = vector<long long>;
using mat = vector<vector<int>>;
using matll = vector<vector<long long>>;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define all(v) v.begin(), v.end()
#define endl "\n"
#define _GLIBCXX_DEBUG
constexpr int MOD = 1000000007;
const int INF = 1 << 30;
template <typename T>
T gcd(T a, T b) { return b ? gcd(b, a % b) : a; }
template <typename T>
T lcm(T a, T b) { return a / gcd(a, b) * b; }

int main(){
    int l, q;
    cin >> l >> q;
    set<int> pos;
    pos.insert(0);
    pos.insert(l);
    rep(i, q){
        int c, x;
        cin >> c >> x;
        if(c==1){   
            pos.insert(x);
        }
        else{
            auto it = pos.lower_bound(x);
            int right = *it;
            int left = *--it;
            cout<<right-left<<endl;
        }
    }
}