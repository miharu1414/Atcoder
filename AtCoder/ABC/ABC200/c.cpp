#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using pii = pair<int, int>;
using pll = pair<long long, long long>;
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
template <typename T> T gcd(T a, T b) { return b ? gcd(b, a % b) : a; }
template <typename T> T lcm(T a, T b) { return a / gcd(a, b) * b; }

ll conbination(int z){
    ll sum =0;
    for(int i =1;i<z;i++) sum += i;
    return sum;
}
int main() {
    int n;
    cin >> n;
    vector<ll> mod200(200,0);
    rep(i, n){
        int A;
        cin>>A;
        mod200[A%200]++;
    }
    ll ans =0;
    for(int i = 0;i<200;i++){
        int sum_mod200 = 0;
        sum_mod200 = mod200[i];
        if(sum_mod200==0||sum_mod200==1) continue;
        ans += conbination(sum_mod200);
    }
    cout<<ans<<endl;

}