#include <bits/stdc++.h>
#include <atcoder/all>
#include <time.h>


using namespace std;
using namespace atcoder;

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



const long long INF = 1LL << 60;
const int inf = 1<<30;
template <typename T>
T gcd(T a, T b) { return b ? gcd(b, a % b) : a; }
template <typename T>
T lcm(T a, T b) { return a / gcd(a, b) * b; }


int sum(vector<int> v){
	int sum = 0;
	for(int i = 0;i<v.size();i++) sum += v[i];
	return sum;
}
double sum(vector<double> v){
	double sum = 0;
	for(int i = 0;i<v.size();i++)  sum += v[i];
	return sum;
}

using mint = modint998244353;






const int MAX = 510000;
const int MOD = 998244353;

long long fac[MAX], finv[MAX], inv[MAX];

// テーブルを作る前処理
void COMinit() {
    fac[0] = fac[1] = 1;
    finv[0] = finv[1] = 1;
    inv[1] = 1;
    for (int i = 2; i < MAX; i++){
        fac[i] = fac[i - 1] * i % MOD;
        inv[i] = MOD - inv[MOD%i] * (MOD / i) % MOD;
        finv[i] = finv[i - 1] * inv[i] % MOD;
    }
}

// 二項係数計算
long long COM(int n, int k){
    if (n < k) return 0;
    if (n < 0 || k < 0) return 0;
    return fac[n] * (finv[k] * finv[n - k] % MOD) % MOD;
}
int main() {
    int n,k;
    cin>>n>>k;
    // 前処理
    COMinit();
    mint ans = 0;
    if(k<(n+1)/2){
        cout<<0<<endl;
        return 0;
    }

    else{
        int yobun = k - (n+1)/2;
        ans = COM(n/2,yobun);
        int ans2 =  COM(n/2,yobun);
        if(ans2==0){
            cout<<1<<endl;
            return 0;
        }
        cout<<ans.val()<<endl;

    }

}