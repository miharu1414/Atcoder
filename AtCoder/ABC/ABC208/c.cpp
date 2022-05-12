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
    ll n, k;
    cin >> n >> k;
    ll fair = k / n;
    ll amari = k % n;
    vector<ll> a(n);
   
    map<ll, ll> a_id,a_num;
    rep(i, n) {
        cin >> a[i];
        a_id[i] = a[i];
        a_num[a[i]] = fair;
  
    }
    sort(all(a));
    for(int i = 0; i < amari; i++)    a_num[a[i]]++;
    for(int i = 0; i < n; i++) cout<<a_num[a_id[i]]<<endl;
    
}
