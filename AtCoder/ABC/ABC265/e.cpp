#include <bits/stdc++.h>
#include <atcoder/all>
#include <time.h>


clock_t start = clock();
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




using mint = modint998244353;

int main() {
    int n,m;
    cin>>n>>m;
    int a,b;
    vector<pair<int,int>> dxy;
    rep(i,3){
        cin>>a>>b;
        dxy.push_back({a,b});
    }

    set<pair<int,int>> S;
    rep(i,m){
        int x,y;
        cin>>x>>y;
        S.insert(make_pair(x,y));
    }

    map<pair<ll,ll>,mint> dp;
    dp[{0,0}]= 1;
    for(int i = 0;i<n;i++){
        map<pair<ll,ll>,mint> new_dp;
        for(auto [xy,val]:dp){
            auto [x,y] = xy;
            for(auto[dx,dy]:dxy){
                if(S.find({x+dx,y+dy})==S.end()){
                    new_dp[{x+dx,y+dy}]+=val;
                }
            }
        }
        swap(dp,new_dp);
    }

    mint ans = 0;
    for(auto[xy,val]:dp){
        ans += val;
    }
    cout<<ans.val()<<endl;
    



}