#include <bits/stdc++.h>     
using namespace std;
using ll = long long;
using vec = vector<int>;
using vecll = vector<long long>;
#define rep(i, n) for(int i = 0; i < (int)(n); i++)
#define all(v) v.begin(), v.end()
#define endl "\n"
#define _GLIBCXX_DEBUG
 
 constexpr int MOD = 1000000007;
 const int INF = 1 << 30;
   
  int main(){
       int n;
       cin >> n;
       vecll s(n), ans(n);
       ll mint = 1000000007,nummint;
       rep(i, n) cin >> s[i];
       rep(i, n){
            cin >> ans[i];
            if(mint>ans[i]){
                nummint = i;
                mint = ans[i];
            }
       }
       

       for (int i = nummint; i < n; i++){
           if(i!=n-1){
               ans[i + 1] = min(ans[i + 1], ans[i] + s[i]);
           }
           else    ans[0] = min(ans[0], ans[i] + s[i]);
       }
       if(nummint==0){
               rep(i, n) cout << ans[i] << endl;
               return 0;
       }
       for (int i = 0; i < nummint;i++){
           if(i!=n-1){
               ans[i + 1] = min(ans[i + 1], ans[i] + s[i]);
           }
           else    ans[0] = min(ans[0], ans[i] + s[i]);
       }
       rep(i, n) cout << ans[i] << endl;
   }
       