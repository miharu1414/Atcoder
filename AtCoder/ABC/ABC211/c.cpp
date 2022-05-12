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

template <unsigned int MOD>
 struct ModInt {
     using uint = unsigned int;
     using ull = unsigned long long;
     using M = ModInt;
  
     uint v;
  
     ModInt(ll _v = 0) { set_norm(_v % MOD + MOD); }
     M& set_norm(uint _v) {  //[0, MOD * 2)->[0, MOD)
         v = (_v < MOD) ? _v : _v - MOD;
         return *this;
     }
  
     explicit operator bool() const { return v != 0; }
     M operator+(const M& a) const { return M().set_norm(v + a.v); }
     M operator-(const M& a) const { return M().set_norm(v + MOD - a.v); }
     M operator*(const M& a) const { return M().set_norm(ull(v) * a.v % MOD); }
     M operator/(const M& a) const { return *this * a.inv(); }
     M& operator+=(const M& a) { return *this = *this + a; }
     M& operator-=(const M& a) { return *this = *this - a; }
     M& operator*=(const M& a) { return *this = *this * a; }
     M& operator/=(const M& a) { return *this = *this / a; }
     M operator-() const { return M() - *this; }
     M& operator++(int) { return *this = *this + 1; }
     M& operator--(int) { return *this = *this - 1; }
  
     M pow(ll n) const {
         if (n < 0) return inv().pow(-n);
         M x = *this, res = 1;
         while (n) {
             if (n & 1) res *= x;
             x *= x;
             n >>= 1;
         }
         return res;
     }
  
     M inv() const {
         ll a = v, b = MOD, p = 1, q = 0, t;
         while (b != 0) {
             t = a / b;
             swap(a -= t * b, b);
             swap(p -= t * q, q);
         }
         return M(p);
     }
  
     bool operator==(const M& a) const { return v == a.v; }
     bool operator!=(const M& a) const { return v != a.v; }
     friend ostream& operator<<(ostream& os, const M& a) { return os << a.v; }
     static uint get_mod() { return MOD; }
 };
  using Mint = ModInt<1000000007>;
int main(){
    string s;
    cin>>s;
    vector<Mint> dp(8,0);
    int len = s.size();
    map<char,int> a;
    a['c']=0;
    a['h']=1;
    a['o']=2;
    a['k']=3;
    a['u']=4;
    a['d']=5;
    a['a']=6;
    a['i']=7;
    for(int i =0;i<len;i++){
        if(s[i]=='c'){
            dp[0]++;
        }
        else if(a.count(s[i])){
            dp[a.at(s[i])]=dp[a.at(s[i])-1]+dp[a.at(s[i])];
        }
    }
    cout<<dp[7]<<endl;
    
}