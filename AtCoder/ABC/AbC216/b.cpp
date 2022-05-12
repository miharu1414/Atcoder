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
    int n;
    cin>>n;
    vector<string> s(n),t(n);
    rep(i,n) cin>>s[i]>>t[i];
    rep(i,n){
        rep(j,n){
                if(i==j)continue;
                if(s[i]==s[j]&&t[i]==t[j]){
                    cout<<"Yes"<<endl;
                    return 0;
                }
        }
    }
    cout<<"No"<<endl;
}