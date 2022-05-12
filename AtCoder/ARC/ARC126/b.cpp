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



bool hantei(ll k,vector<pair<int,int>> x,vector<pair<int,int>> y){
    ll cnt =0,pre=0;

}


int main() {
   int n,m;
   cin>>n>>m;
   vector<int> a(m),b(m);
   vector<pair<int,int>> ab(m),ba(m);
   rep(i,m){
       cin>>a[i]>>b[i];
        ab[i]=make_pair(a[i],b[i]);
        ba[i]= make_pair(b[i],a[i]);
   }
   ll left = =1;
   ll right = m+1;
   
   while(right - left >1){
       ll mid = left + (right - left )/2;
       if(hantei(mid,ab,ba)) left = mid;
       else right = mid;
   }
}