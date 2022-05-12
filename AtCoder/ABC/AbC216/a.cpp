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
    double x;
    cin>>x;
    int y = floor((double)x);
    double d = x*10-y*10;
    cout<<y;
    if(d>=0&&d<=2){
        cout<<"-"<<endl;
    }
    else if(3<=d&&d<=6){
        cout<<endl;
    }
    else cout<<'+'<<endl;
}