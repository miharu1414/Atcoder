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
    int n, k, ans;
    cin >> n >> k;
    vec c(n);
    rep(i, n) cin >> c[i];
    map<int, int> candy_kind;
    for(int i = 0; i < k; i++) {
        if(candy_kind.count(c[i])) { //すでに所属していたら1を足す．
            candy_kind[c[i]] += 1;
        } else
            candy_kind[c[i]] = 1;
    }
    ans = candy_kind.size();
    for(int i = k; i < n; i++) {
        if(candy_kind[c[i - k]] == 1)
            candy_kind.erase(
                c[i - k]); //削除される値しかその種類の飴が入っていない場合
        else
            candy_kind[c[i - k]] -= 1;
        if(candy_kind.count(c[i])) { //すでに所属していたら1を足す．
            candy_kind[c[i]] += 1;
        } else
            candy_kind[c[i]] = 1;
        int a = candy_kind.size();
        ans = max(ans, a);
    }
    cout << ans << endl;
}