#include <bits/stdc++.h>
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
#define absolute(a) max(a, -a)

constexpr int MOD = 1000000007;
const int INF = 1 << 30;

template <typename T>
T gcd(T a, T b) { return b ? gcd(b, a % b) : a; }
template <typename T>
T lcm(T a, T b) { return a / gcd(a, b) * b; }

int main(){
    int n, m;
    cin >> n >> m;
    vec a(n), b(m);
    for (int i = 0; i < n; i++){
        cin >> a[i];
    }
    rep(i, m) cin >> b[i];
    sort(all(a));
    sort(b.begin(), b.end());
    int x = 0, y = 0;
    int ans = INF;
    while ((x < n) && (y < m)){
        ans = min(ans, abs(a[x] - b[y]));
        if(a[x]>b[y])y++;
        else        x++;
    }
    cout << ans << endl;
}