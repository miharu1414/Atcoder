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
       int a, b;
       cin >> a >> b;
       vec A(8), B(8);
       int i = 7;

       while (i>=0)
       {
           A[i] = a / (1 << i);
           B[i] = b / (1 << i);
           a %= 1 << i;
           b %= 1 << i;
           i--;
       }
       vec ans(8);
       rep(i, 8){
           if(A[i]==B[i]) ans[i] = 0;
           else ans[i] = 1;
       }
       int an = 0;
       rep(i,8){
           an += ans[i] * (1 << i);
       }
       cout << an << endl;
   }