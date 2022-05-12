#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using pii = pair<int, int>;
using Pll = pair<long long,long long>;
using vec = vector<int>;
using vecll = vector<long long>;
using mat = vector<vector<int>>;
using matll = vector<vector<long long>>;
#define rep(i, n) for(int i = 0; i < (int)(n); i++)
#define all(v) v.begin(), v.end()
#define endl "\n"
#define _GLIBCXX_DEBUG
#define absolute(a) max(a,-a)

constexpr int MOD = 1000000007;
const int INF = 1 << 30;

template<typename T> T gcd(T a, T b) { return b ? gcd(b, a%b) : a; }
template<typename T> T lcm(T a, T b) { return a / gcd(a, b) * b ;}

int main(){
    int n;
    string t;
    cin>>n>>t;
    int x = 0,y =0;
    int now = 1;
    rep(i,n){
        if(t[i]=='S'){
            if (now == 1){
                x++;
            }
            else if(now == 2){
                y--;
            }
            else if(now == 3){
                x--;
            }
            else if(now == 4){
                y++;
            }
        }
        else{
            if (now == 1){
                now = 2;
            }
            else if(now == 2){
                now = 3;
            }
            else if(now == 3){
                now = 4;
            }
            else if(now == 4){
                now = 1;
            }
        }
    }
    cout<<x<<' '<<y<<endl;
}