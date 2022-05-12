#include <bits/stdc++.h>     
using namespace std;
using ll = long long;
using pii = pair<int, int>;
using pll = pair<long long,long long>;
using vec = vector<int>;
using vecll = vector<long long>;
using mat = vector<vector<int>>;
using matll = vector<vector<long long>>;
#define rep(i, n) for(int i = 0; i < (int)(n); i++)
#define all(v) v.begin(), v.end()
#define endl "\n"
#define _GLIBCXX_DEBUG
constexpr int MOD = 1000000007;
const int INF = 1 << 30;
template<typename T> T gcd(T a, T b) { return b ? gcd(b, a%b) : a; }
template<typename T> T lcm(T a, T b) { return a / gcd(a, b) * b ;}
int main(){
    ll n;
    cin>>n;
    ll a=0,b=0;
    b = n % 2;
    a =  n/2;
    vector<ll> ans;
    bool ok = true;
    while(ok){
        if(n %2 == 1){
            n -= 1;
            ans.push_back(1);
        }
        if(n==0) break;
        ans.push_back(0);
        n /= 2;

    }
    for(int i = ans.size()-1;i>=0;i--){
        if(ans[i]==1) cout<<"A";
        else cout<<"B";
    }

}