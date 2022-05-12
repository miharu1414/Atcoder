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

long long int f(long long a, long long b){
    return (a*a*a+a*a*b+a*b*b+b*b*b);
}

int main() {
    ll n;
    cin>>n;
    ll ans = INF;
    ll j = 1000000;
    for(int i = 0;i< 1000000;i++){
        while(f(i,j)>=n && j >= 0 ){
            ans = min(ans,f(i,j));
            j--;
        }
    }
    cout<<ans<<endl;
}