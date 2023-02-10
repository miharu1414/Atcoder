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
#define INF 1<<60
#define inf 1<<30
// using mod = modint1000000007;
// using mod = modint998244353;
#define __SPEED_UP__                  \
    ios_base::sync_with_stdio(false); \
    cin.tie(nullptr);





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

/* warshall_floyd(dist)
    入力：初期化した dist
    計算量：O(|V|^3)
    副作用：dis[i][j]にiからjへの最短路のコストを格納
*/
void warshall_floyd(vector<vector<long long>> &dist,vector<vector<long long>> &score) {
    int V = dist.size();
    for (int k = 0; k < V; k++) {
        for (int i = 0; i < V; i++) {
            for (int j = 0; j < V; j++) {
				if(dist[i][j]>dist[i][k] + dist[k][j]){
					dist[i][j] =dist[i][k] + dist[k][j];
					score[i][j] =score[i][k] + score[k][j];
				}
				if((dist[i][j]==dist[i][k] + dist[k][j]) && (score[i][j] <score[i][k] + score[k][j])){
					score[i][j] =score[i][k] + score[k][j];
				}
                
            }
        }
    }
}

int main() {
	int n;
	cin>>n;
	vector<ll> a(n);
	rep(i,n) cin>>a[i];
	vector<string> s(n);
	rep(i,n) cin>>s[i];
	int q;
	cin>>q;
	vector<ll> u(q),v(q);
	rep(i,q) cin>>u[i]>>v[i];
     // 頂点数
	
vector<vector<long long>> dist (n,vector<long long> (n,1<<30));
vector<vector<long long>> score (n,vector<long long> (n,-1));
    // 更新
    // 出力
	for (int i =  0;i<n;i++){
		rep(j,n){
			if(s[i][j] =='Y'){
				dist[i][j] = 1;
				score[i][j] = a[j];
		}
	}
	}
    warshall_floyd(dist,score);  
	rep(i,q){
		if (dist[u[i]-1][v[i]-1]==1<<30) cout<<"Impossible"<<endl;
		else cout<<dist[u[i]-1][v[i]-1]<<' '<<a[u[i]-1]+score[u[i]-1][v[i]-1]<<endl;
	}

}