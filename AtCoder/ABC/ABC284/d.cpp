#include <bits/stdc++.h>
#include <atcoder/all>
#include <time.h>

using namespace atcoder;
using namespace std;
#define _GLIBCXX_DEBUG

using ll = long long;
using pii = pair<int, int>;
using Pll = pair<long long, long long>;
using vec = vector<int>;
using vecll = vector<long long>;
using Graph = vector<vector<int>>;
using Graphll = vector<vector<long long>>;
using mat = vector<vector<int>>;
using matll = vector<vector<long long>>;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define rep2(i, m, n) for (ll i = (ll)(m); i < (ll)(n); i++)

#define forall(i, v) for (auto& i : v)
#define forallpair(i, j, v) for (auto& [i, j] : v)

#define all(v) v.begin(), v.end()
#define YesNo(a) ((a) ? "Yes" : "No")
#define YESNO(a) ((a) ? "YES" : "NO")
#define yesno(a) ((a) ? "yes" : "no")

// using mod = modint1000000007;
// using mod = modint998244353;
#define __SPEED_UP__                  \
    ios_base::sync_with_stdio(false); \
    cin.tie(nullptr);


constexpr int MOD = 1000000007;
const long long INF = 1LL << 60;
const int inf = 1<<30;

template <typename T>
T gcd(T a, T b) { return b ? gcd(b, a % b) : a; }
template <typename T>
T lcm(T a, T b) { return a / gcd(a, b) * b; }

template <typename T>
long long sum(vector<T> v){
	ll Sum = 0;
	for(int i = 0;i<v.size();i++) Sum += v[i];
	return Sum;}
double sum(vector<double> v){
	double Sum = 0;
	for(int i = 0;i<v.size();i++)  Sum += v[i];
	return Sum;}
double Min(vector<double> v){
	double ans = v[0];
	for(int i = 0;i<v.size();i++) ans = min(ans,v[i]);
	return ans;}
double Max(vector<double> v){
	double ans = v[0];
	for(int i = 0;i<v.size();i++) ans = max(ans,v[i]);
	return ans;}
int Min(vector<int> v){
	int ans = v[0];
	for(int i = 0;i<v.size();i++) ans = min(ans,v[i]);
	return ans;}
int Max(vector<int> v){
	int ans = v[0];
	for(int i = 0;i<v.size();i++) ans = max(ans,v[i]);
	return ans;}
long long Min(vector<long long> v){
	long long ans = v[0];
	for(int i = 0;i<v.size();i++) ans = min(ans,v[i]);
	return ans;}
long long Max(vector<long long> v){
	long long ans = v[0];
	for(int i = 0;i<v.size();i++) ans = max(ans,v[i]);
	return ans;}

//using mint = modint998244353;
using mint = modint1000000007;
// 1 以上 N 以下の整数が素数かどうかを返す
vector<bool> Eratosthenes(int N) {
    // テーブル
    vector<bool> isprime(N+1, true);

    // 0, 1 は予めふるい落としておく
    isprime[0] = isprime[1] = false;

    // ふるい
    for (int p = 2; p <= N; ++p) {
        // すでに合成数であるものはスキップする
        if (!isprime[p]) continue;

        // p 以外の p の倍数から素数ラベルを剥奪
        for (int q = p * 2; q <= N; q += p) {
            isprime[q] = false;
        }
    }

    // 1 以上 N 以下の整数が素数かどうか
    return isprime;
}

int main() {
	__SPEED_UP__
    // 50 以下の素数をすべて求める
    vector<bool> isprime = Eratosthenes(10000000);
	vector<ll> sosuu;
	set<ll> issosuu;
	for(int i = 0;i<=10000000;i++){
		if(isprime[i]==1){
			sosuu.push_back(i);
			issosuu.insert(i);
		}
	}

	set<ll> heihousuu;
	rep(i,sosuu.size()){
		heihousuu.insert(sosuu[i]*sosuu[i]);
	}
	int t;
	cin>>t;
	ll n;
	ll p;
	ll q;
	rep(i,t){
	
		cin>>n;
		int j = 0;
		while(1){
			p = sosuu[j];
			if(n%(p*p)==0){
				q = n/p/p;
				if(issosuu.count(q) ){
					cout<<p<<' '<<q<<endl;
					break;
				}
			}
			else if(n%p==0){
				ll q = n/p;
				if(heihousuu.count(q)){
					cout<<(int)sqrt(q)<<' '<<p<<endl;
					break;
				}

			}
			j++;
		}
	}

}
