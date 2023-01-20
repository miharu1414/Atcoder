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

int main() {
	__SPEED_UP__
	int n,m,x;
	cin>>n>>m>>x;
	vector<int> c(n);
	mat a(n,vector<int> (m));
	rep(i,n){
		cin>>c[i];
		rep(j,m){
			cin>>a[i][j];
		}
	}
	int ans =1<<30;

	for (int bit = 0; bit < (1<<n); ++bit) {
        vector<int> score_m(m,0);
		int flag =1, cost = 0;
        for (int i = 0; i < n; ++i) {
            if (bit & (1<<i)) { // 列挙に i が含まれるか
                rep(k,m){
					score_m[k] += a[i][k];
				}
				cost += c[i];
            }
		}
		rep(i,m){
			if(score_m[i]<x){
				flag = 0;
				break;
			}
		}
		if (flag) ans = min(ans,cost);
    }
	if (ans == 1<<30) cout<<-1<<endl;
	else cout<< (ans)<<endl;
		
}
