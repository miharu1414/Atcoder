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
	return Sum;
}
double sum(vector<double> v){
	double Sum = 0;
	for(int i = 0;i<v.size();i++)  Sum += v[i];
	return Sum;
}






int main() {
	/*
	int n,m;
	cin>>n>>m;
	vector<ll> a(n);
	rep(i,n) cin>>a[i];
	vector<vector<ll>> dp(n+1,vector<ll> (n+1));
	dp[0][0] = 0;
	dp[0][1] = -100000000000000ll;
	for(int i = 1;i<=n;i++){
		for(int j = 0;j<=n;j++){
			if(j==0) dp[i][0] = 0;
			else if(j>i) dp[i][j] = -100000000000000LL;
			else{
				dp[i][j] = max(dp[i-1][j],dp[i-1][j-1] + j*a[i-1]);
			}
		}
	}

	cout<<dp[n][m]<<endl;
	*/


	int n; cin>>n;
	vector<int> a(n);
	rep(i,n)  cin>>a[i];
	cout<<sum(a)<<endl;
}