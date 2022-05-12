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
const int INF = 1 << 30;

template <typename T>
T gcd(T a, T b) { return b ? gcd(b, a % b) : a; }
template <typename T>
T lcm(T a, T b) { return a / gcd(a, b) * b; }


int main() {
 int t;
    cin>>t;
    rep(i,t){
        ll n2,n3,n4;
        cin>>n2>>n3>>n4;
  
        ll pairn3 = n3/2;
        ll count =0 ;
        if(pairn3>0&&n4>0){
            ll min34 = min(pairn3,n4);
            pairn3 -= min34;
            n4 -= min34; 
            count += min34;
        }
       
        if(n4>1&&n2>0){
            ll min24 = min(n4/2,n2);
            n4 -= 2*min24;
            n2 -= min24;
            count += min24;
        }
         
        
        if(pairn3>0&&n2>1){
            ll min23 = min(pairn3,n2/2);
            pairn3 -= min23;
            n2 -= 2*min23;
            count += min23;
        }
        if(n4>0&&n2>1){
            ll min24 = min(n4,n2/3);
            n4 -= min24;
            n2 -= min24*3;
            count += min24;
        }
        if(n2>4){
            ll make2_5 = n2/5;
            count += make2_5;
        }
        cout<<count<<endl;
    }

}