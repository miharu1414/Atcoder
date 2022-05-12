#include <bits/stdc++.h>
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
#define absolute(a) max(a, -a)

constexpr int MOD = 1000000007;
const int INF = 1 << 30;

template <typename T>
T gcd(T a, T b) { return b ? gcd(b, a % b) : a; }
template <typename T>
T lcm(T a, T b) { return a / gcd(a, b) * b; }

int main(){
    vector<string> s(4);
    rep(i,4) cin>>s[i];
    set<string> a;
    a.insert("H");
    a.insert("2B");
    a.insert("3B");
    a.insert("HR");
    bool ans = false;
    int count=0;
    rep(i,4){
        if(a.count(s[i])){
            a.erase(s[i]);
            count++;
        }
    }
    cout<<(count==4?"Yes":"No")<<endl;

    
}