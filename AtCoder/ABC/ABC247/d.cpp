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
    int q;
    cin>>q;
    vecll x(q,0),num(q,0);
    ll s,X,c;
    int box_count = 0;
    int now = 0;
    rep(i,q){
        cin>>s;
        if(s==1){
            cin>>X>>c;
            x[box_count] = X;
            num[box_count] = c;
            box_count++;
        }
        else{
            ll ans = 0;
            cin>>c;
            while(num[now]<c){
                ans += num[now]*x[now];
                c -= num[now];
                num[now] = 0;
                now ++;
            }
            ans += x[now]*c;
            num[now] -= c;
            cout<<ans<<endl;
        }
    }
}