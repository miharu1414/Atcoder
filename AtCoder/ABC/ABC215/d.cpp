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

vector<pair<long long, long long> > prime_factorize(long long N) {
    vector<pair<long long, long long> > res;
    for (long long a = 2; a * a <= N; ++a) {
        if (N % a != 0) continue;
        long long ex = 0; // 指数

        // 割れる限り割り続ける
        while (N % a == 0) {
            ++ex;
            N /= a;
        }

        // その結果を push
        res.push_back({a, ex});
    }

    // 最後に残った数について
    if (N != 1) res.push_back({N, 1});
    return res;
}

int main() {
    long long N,M;
    cin >> N >>M;
 
    set<int> douda;
    vector<int> A(N);
    rep(i,N) cin>>A[i];
    for(int j =0;j<N;j++){
    const auto &res = prime_factorize(A[j]);
    for (auto p : res) {
        for (int i = 0; i < p.second; ++i) douda.insert(p.first);
    }
    }
    if(douda.count(1)) douda.erase(1);
    ll ans =0;
    vec a;
    for(int i = 2;i<=M;i++){
        if(douda.count(i)) continue;
        const auto &res = prime_factorize(i);
        bool w = true;
    for (auto p : res) {
        for (int j = 0; j < p.second; ++j) if(douda.count(p.first)){
            w = false;
            break;
        }
        if(w==false) break;
    }
    if(w){
        ans ++;
        a.push_back(i);
    }

    }
    cout<<ans+1<<endl;
    cout<<1<<endl;
    for(auto x:a){
        cout<<x<<endl;
    }
}