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
#define Rep(i,l,r) for(int i=l;i<=r;i++)
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
    ll n, k,ans=0;
    cin>>n>>k;
    vector<ll> a(n);
    vector<ll> ruiseki(n+1);
    ruiseki[0]=0;
    rep(i,n){
        cin>>a[i];
        ruiseki[i+1] = ruiseki[i]+a[i]; 
    }
    map<ll,ll> mp;
    Rep(i,1,n){
        mp[ruiseki[i-1]]++;
        ans += mp[ruiseki[i]-k];
    }
    cout<<ans<<endl;
}