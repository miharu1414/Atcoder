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

    int n,k,x;
    cin>>n>>k>>x;
    vec a(n);
    rep(i,n) cin>>a[i];
    sort(all(a));

    rep(i,n){
        if(k==0) break;
        int use = a[n-i-1] / x;
        if(use>k){
            use = k;
        }
        a[n-i-1] -= x * use;
        k-= use;
    }
        sort(all(a));
    for(int j = 0;j<k;j++){
        if(j>=n)break;
        a[n-j-1] = 0;
    }
    long long ans = 0;
    rep(i,n) ans+=a[i];
    cout<<ans;
}