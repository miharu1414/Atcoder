#include <bits/stdc++.h>
#include <atcoder/all>
#include <time.h>



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








int start, goal;
bool visited[3005];
	
    mat G(3005);

bool dfs(int x){
    visited[x] = true;
    if(x == goal) return true;
    for(auto v: G[x]){
        if(visited[v]) continue;
        if(dfs(v)) return true;
    }
    return false;
}    




ll d(ll x,ll y,ll x1,ll y1){
    ll sum = (x-x1)*(x-x1)+(y-y1)*(y-y1);
	return sum;
}


ll jou(ll x){
    return x*x;
}

int main() {
    int n;
    cin>>n;
    ll sx,sy,tx,ty;
    cin>>sx>>sy>>tx>>ty;
    vector<ll> x(n),y(n),r(n);
    rep(i,n) cin>>x[i]>>y[i]>>r[i];

    rep(i,n){
        for(int j = i+1;j<n;j++){
            if (jou(r[i]-r[j])<d(x[i],y[i],x[j],y[j]) && d(x[i],y[i],x[j],y[j]) < jou(r[i]+r[j])){
                G[i].push_back(j);
                G[j].push_back(i);
            }
            else if(d(x[i],y[i],x[j],y[j]) == jou(r[i]+r[j])){
                G[i].push_back(j);
                G[j].push_back(i);
            }        
            else if(d(x[i],y[i],x[j],y[j]) == jou(r[i]-r[j])){
                G[i].push_back(j);
                G[j].push_back(i);
            }
    }
    }

    //スタートとゴールとなる頂点を求める

    rep(i,n){
        if(jou(x[i]-sx)+jou(y[i]-sy) == jou(r[i])){
            start = i;
        }
        if(jou(x[i]-tx)+jou(y[i]-ty) == jou(r[i])){
            goal = i;
        }
    }

    if(dfs(start)){
        cout<<"Yes"<<endl;
    }
    else{
        cout<<"No"<<endl;
    }
}