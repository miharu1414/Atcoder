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
    cin>>n;
    vector<int> num(2*n+1);
    rep(i,2*n+1) num[i]= i+1;
    set<int> count;
    num.erase(num.begin());
    count.insert(1);
    cout<<1<<endl;
    for(int i = 0;i<=n;i++){
        int x,y;
  
        cin>>x;
        count.insert(x);
        int j = 2;
        if(x==0) break;
        while(1){
            if(!count.count(j)){
                count.insert(j);
                cout<<j<<endl;
                break;
            }
            j++;
        }
        
    }
}