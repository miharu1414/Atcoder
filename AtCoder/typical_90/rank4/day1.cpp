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


int l,n,k;
long long a[1<<18];

bool solve(int m){
    int pre =0, cut_cnt=0;
    for(int i =0;i<n;i++){ 
        if(a[i]-pre>=m && l-a[i]>=m){
            pre = a[i];
            cut_cnt++;
            }
    }
    if(cut_cnt>=k) return true;
    return false;
}

int main(){

    cin>>n>>l>>k;
    
    for(int i =0;i<n;i++)      cin>> a[i];

    //二分探索
    int right = l+1, left = -1;
    while(right - left >1){
        int mid = left + (right - left)/2;
        if(solve(mid)) left = mid;
        else right = mid;
    }
    cout<<left<<endl;





    }