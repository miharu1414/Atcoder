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
    vector<ll> a(n);
    int count_1=0;
    rep(i,n){
        cin>>a[i];
        if(a[i]==1) count_1++;
    }
    bool ok = false;
    if(n==1 && a[0]==1) ok = false;
    else if(count_1==0) ok =true;
    else if(a[1]==1) ok = true;

    if(ok)cout<<"Yes";
    else cout<<"No"<<endl;

}