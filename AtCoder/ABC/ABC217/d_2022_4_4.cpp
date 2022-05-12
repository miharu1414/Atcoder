#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using ll = long long;
using pii = pair<int, int>;
using pll = pair<long long, long long>;
using vec = vector<int>;
using vecll = vector<long long>;
using mat = vector<vector<int>>;
using matll = vector<vector<long long>>;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define all(v) v.begin(), v.end()
#define endl "\n"
#define _GLIBCXX_DEBUG
constexpr int MOD = 1000000007;
const int INF = 1 << 30;
template <typename T>
T gcd(T a, T b) { return b ? gcd(b, a % b) : a; }
template <typename T>
T lcm(T a, T b) { return a / gcd(a, b) * b; }

int main(){
    int l,q;
    cin>>l>>q;
    set<int> ans;
    ans.insert(0);
    ans.insert(l);

    for(int i = 0;i<q;i++){
        int c,x;
        cin>>c>>x;
        if(c == 1){
            ans.insert(x);
        }
        else{
            auto it = ans.lower_bound(x);
            auto right = *it;
            auto left = *(--it);
            cout<<right-left<<endl;

        }
    }
}
