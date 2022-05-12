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
    vec x(3),y(3);
    map<int,int> z;
    map<int,int> zy;
    rep(i,3) {
        cin>>x[i]>>y[i];
        if(z.count(x[i])) z[x[i]]++;
        else z[x[i]]=1;
        if(zy.count(y[i])) zy[y[i]]++;
        else zy[y[i]]=1;
        
    }
    int ansx,ansy;
    rep(i,3){
        if(z[x[i]]==1) ansx=x[i];
        if(zy[y[i]]==1) ansy= y[i];
    }
    cout<<ansx<<' '<<ansy;
}