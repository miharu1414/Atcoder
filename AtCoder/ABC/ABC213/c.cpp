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
       int h, w, n;
       cin >> h >> w >> n;
       vector<int> x(n),y(n),x1,y1;
       rep(i, n) cin >> x[i] >> y[i];
       set<int> x_set, y_set;
       for (int i = 0; i < n; i++) {
           if(x_set.count(x[i])){

            }
           else{
                x_set.insert(x[i]);
                x1.push_back(x[i]);
            }
           if(y_set.count(y[i])){

            }
           else{
                y_set.insert(y[i]);
                y1.push_back(y[i]);
            }
       }
       sort(all(y1));
       sort(all(x1));
       map<int, int> xans, yans;
       for (int i = 0; i < x1.size(); i++){
           xans[x1[i]] = i+1;
       }
        for (int i = 0; i < y1.size(); i++){
           yans[y1[i]] = i+1;
       }
       for (int i = 0; i < n;i++){
           cout << xans[x[i]] << " " << yans[y[i]] << endl;
       }
   }
