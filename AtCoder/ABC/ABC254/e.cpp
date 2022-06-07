#include <bits/stdc++.h>
#include <atcoder/all>

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


int main() {
        int n,m;
        cin>>n>>m;
        vector<vector<int>> G(n+1);
        rep(i,m){
            int a,b;
            cin>>a>>b;
            G[a].push_back(b);
            G[b].push_back(a);
        }
        
        int q;
        cin>>q;
        vec A(q);
        rep(i,q){
            int x,k;cin>>x>>k;
            vector<vector<int>> nodes(4);
            vector<int> dist(n+1,-1);
            dist[x] = 0;
            nodes[0].push_back(x);
            int ans = x;
            for(int z = 1;z<k+1;z++){
                for(auto v:nodes[z-1]){
                    for(auto next_v : G[v]){
                        if(dist[next_v]!=-1) continue;
                        dist[next_v] = dist[v] +1;
                        nodes[z].push_back(next_v); 
                        ans += next_v;
                }
            }
        }
                    A[i] = ans;
        }
        for(auto x: A) cout<<x<<endl;


}