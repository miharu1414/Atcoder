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
    vector<pair<int,int>> lr(n);
    rep(i,n){
        cin>>lr[i].first>>lr[i].second;
    }
    sort(all(lr));
    rep(i,n) cout<<lr[i].first<<lr[i].second<<endl;

    if(n ==1){
        cout<<lr[0].first<<' '<<lr[0].second<<endl;
        return 0;
    }

    int left,right, now_i, right_pos;
    left = lr[0].first;
    right = lr[0].second;
    right_pos = 0;
    now_i = 1;

    while(1){
        if (lr[now_i].first<= lr[right_pos].second){
            if (lr[now_i].second>right){
                right_pos = now_i;
                right = lr[right_pos].second;
            }
            
        }
    }

}