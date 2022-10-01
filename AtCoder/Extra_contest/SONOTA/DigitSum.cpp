//https://atcoder.jp/contests/joi2020yo2/tasks/joi2020_yo2_c

#include <bits/stdc++.h>
#include <atcoder/all>
#include <time.h>

using namespace atcoder;
using namespace std;
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
#define all(v) v.begin(), v.end()
#define endl "\n"
#define _GLIBCXX_DEBUG


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




int main() {
	int n,k;
	cin>>n>>k;
	vector<int> a(n),b(n);
	map<ll,ll> pasta;
	rep(i,k){
		cin>>a[i]>>b[i];
		pasta[a[i]] = b[i]-1;
	}
	int mod  = 10000;


	matll dp(n+1,vector<ll> (3,0));
	for(int i = 1;i<=n;i++){
		if(i == 1){
			if(pasta.count(i)){
				dp[i][pasta[i]] = 1;
			}
			else{
				rep(j,3) dp[i][j] = 1;
			}
		}

		else if(i == 2){
			if(pasta.count(i)){
				rep(j,3) dp[i][pasta[i]] += dp[i-1][j];
			}
			else{
				int sum  = 0;
				rep(j,3) sum += dp[i-1][j] ;
				rep(j,3) dp[i][j] = (dp[i][j] + sum)%mod;

			}
		}
		else{
			if(pasta.count(i)){
					rep(j,3) dp[i][pasta[i]] += dp[i-1][j];
					if(dp[i-1][pasta[i]]>0) dp[i][pasta[i]] -= dp[i-2][pasta[i]];
					dp[i][pasta[i]] %= mod;
				
			}
			else{
				rep(j,3){
					rep(k,3) dp[i][j] += dp[i-1][k];
					if(dp[i-1][j]>0) dp[i][j] -= dp[i-2][j];
					dp[i][j] %= mod;
				}
			}
		}
	
	}
	ll ans = 0;
	rep(j,3) ans  += dp[n][j];
	ans%= mod;
	cout<<ans<<endl;
	
}