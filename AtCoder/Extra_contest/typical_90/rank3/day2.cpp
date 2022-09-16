#include <bits/stdc++.h>
#include <time.h>
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
    clock_t start = clock();

    int  n;
    cin>>n;
       vector<string> s;
       vector<char> a;
    if(n%2==1){
        return 0;
    }
    for(int i =0;i<n;i++){
        if(i%2==0){
            a.push_back('(');
        }
        else a.push_back(')');
    }
    sort(all(a));
    do {
        int cnt_l =0,cnt_r=0;
        bool ok = true;
        for(int i=0;i<n;i++){
            if(a[i]=='('){
                cnt_l++;
            }
            else{
                cnt_r++;
                if(cnt_r>cnt_l){
                    ok = false;
                }

            }

        }

            if(ok){
                string z;
                for(int j=0;j<n;j++){
                    z += a[j];
                }
                s.emplace_back(z);
        }
    } while (next_permutation(a.begin(), a.end()));

    sort(all(s));
    for(auto x: s) cout<<x<<endl; 
  



    

    // 何かの処理

    clock_t end = clock();

    const double time = static_cast<double>(end - start) / CLOCKS_PER_SEC * 1000.0;
    printf("time %lf[ms]\n", time);

    return 0;
}


