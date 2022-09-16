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
T gcd(T *it, T b) { return b ? gcd(b, *it % b) : *it; }
template <typename T>
T lcm(T *it, T b) { return *it / gcd(*it, b) * b; }






int main() {
    int n,k;cin>>n>>k;
    vector<int> p(n),parent(n+1),most_p(n+1),num(n+1);rep(i,n)  cin>>p[i];
    int now;
    set<int> Min;
    now = p[0];
    parent[now] = now;
    most_p[now] = now;
    Min.insert(now);
    num[now] = 1;
    vec ans(n+1,-1);
    if(k==1){
            rep(i,n) ans[p[i]] = i + 1;
                for(int i = 1;i<n+1;i++) cout<<ans[i]<<endl;
                return 0;
    }
    for(int i = 1;i<n;i++){
        now = p[i];
        if(Min.size()==0){
            Min.insert(now);
            num[now] = 1;
            parent[now] = now;
            most_p[now] = now;
            continue;
        }
        auto  it = Min.lower_bound(now);
        if(it == Min.end()){
            Min.insert(now);
            num[now] = 1;
            parent[now] = now;
            most_p[now] = now;
        }
        else{

            int bef = *it;
            Min.erase(bef);
            parent[now] = bef;
            most_p[now] = most_p[bef];
            num[most_p[now]]++;

            if(num[most_p[now]]==k){

                int oya = parent[now];
                while(oya != now){
                    ans[now] = i+1;
                    now = parent[now];
                    oya = parent[now];
                }
                ans[now] = i+1;
            }
            else{
                Min.insert(now);
            }
        }

    }
    for(int i = 1;i<n+1;i++) cout<<ans[i]<<endl;

}