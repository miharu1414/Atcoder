#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using pii = pair<int, int>;
using pll = pair<long long, long long>;
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
template <typename T> T gcd(T a, T b) { return b ? gcd(b, a % b) : a; }
template <typename T> T lcm(T a, T b) { return a / gcd(a, b) * b; }
int main() {
    int n;
    string s;
    cin >> n >> s;
    int cnt = 0, pre = 0;
    rep(i, n) {
        if(s[i] == ')')
            cnt++;
        else
            cnt--;
        pre = max(pre, cnt);
    }
    rep(i, pre) { s = '(' + s; }
    cnt = 0;
    rep(i, n + pre) {
        if(s[i] == '(')
            cnt++;
        else
            cnt--;
    }
    rep(i, cnt) { s = s + ')'; }
    cout << s << endl;
}