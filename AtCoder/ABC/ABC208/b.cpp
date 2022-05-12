#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using pii = pair<int, int>;
using Pll = pair<long long, long long>;
using vec = vector<int>;
using vecll = vector<long long>;
using mat = vector<vector<int>>;
using matll = vector<vector<long long>>;
#define rep(i, n) for(int i = 0; i < (int)(n); i++)
#define all(v) v.begin(), v.end()
#define endl "\n"
#define _GLIBCXX_DEBUG
#define absolute(a) max(a, -a)

constexpr int MOD = 1000000007;
const int INF = 1 << 30;

template <typename T> T gcd(T a, T b) { return b ? gcd(b, a % b) : a; }
template <typename T> T lcm(T a, T b) { return a / gcd(a, b) * b; }

int main() {
    int p;
    cin >> p;
    int ans = 0;
    vector<int> sum(11);
    sum[0]=1;
    for(int i =1;i<11;i++){
        sum[i] = sum[i-1]*(i);
    }
    for(int i =10;i>0;i--){
        int maisu= p/sum[i];
        ans += maisu;
        p -= maisu * sum[i];
    }
    cout<<ans<<endl;
}
