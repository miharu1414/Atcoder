//https://atcoder.jp/contests/joi2012yo/tasks/joi2012yo_d

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






long long d(int x){
	string s = to_string(x);
	int size  = s.size();
	int sum = 0;
	rep(i,size) sum += int(s[i]-'0');
	return sum + x;
}
int main() {
	ll n;cin>>n;



	set<int> N_dig;
	for(int i = n;i>0;i--){
		if(i==n) N_dig.insert(i);
		else{
			if(N_dig.count(d(i))) N_dig.insert(i);
		}
	}
	ll ans = 0;
	rep(i,n){
		if(N_dig.count(i+1)) ans += 1;
	}
	cout<<ans<<endl;
}