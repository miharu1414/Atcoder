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

    ll n,a,b,c;
    cin>>n>>a>>b>>c;
    if (b>a){
        swap(a,b);
    }
    vecll ans;
    if(c>b) swap(c,b);
    if(b>a) swap(a,b);
    for(int i=0;i<10000;i++){
        for(int j = 0;j<10000-i;j++){
            if(a*i+b*j>n)   break;
            if((n-a*i-b*j) %c==0 && (i+j+(n-a*i-b*j)/c)<10000){
                    ans.push_back(i+j+(n-a*i-b*j)/c);
        }
    }
    }
    sort(all(ans));
    cout<<ans[0]<<endl;
}