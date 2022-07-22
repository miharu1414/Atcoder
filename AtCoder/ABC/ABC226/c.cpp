#include <bits/stdc++.h>
#include <atcoder/all>
#include <time.h>
 
 
clock_t start = clock();
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
 
 
 
const int num = 200000;
vec seen(200000,-1);
vec t(num);
vec k(num);
mat G(200000);
vecll memo(200000,-1);

ll rec(int v){
	seen[v] = 1;
	if (k[v] == 0) return memo[v] = t[v];
	if (memo[v]!=-1) return memo[v];
	ll ans = t[v];
	for(auto next_v: G[v]){
		if(seen[next_v] == -1) ans += rec(next_v);
	}
	memo[v] = ans;
	return ans;
}
 
 
 
int main() {
 
	int n;cin>>n;
	rep(i,n){
		cin>>t[i]>>k[i];
		rep(j,k[i]){
			int x;cin>>x;
			G[i].push_back(x-1);
		}
	}
 
	cout<<rec(n-1)<<endl; 
 
}