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
const int INF = 1 << 30;

template <typename T>
T gcd(T a, T b) { return b ? gcd(b, a % b) : a; }
template <typename T>
T lcm(T a, T b) { return a / gcd(a, b) * b; }


int main() {
    string x;
    cin>>x;
    int n;cin>>n;
    map<char,int> alpha;
    rep(i,26){
        alpha[x[i]]=i+1;
    }
    vector<string> s(n);
    int maxsi = -1;
    rep(i,n){
        cin>>s[i];
        int now = s[i].size();
        maxsi = max(now, maxsi);
    }
    ll motoseki =1;
    rep(j,maxsi){
        motoseki *= 27;
    }
    vector<pair<ll,int>> a;
    rep(i,n){
        ll score = 0;
        ll seki = motoseki;
        int si = s[i].size();
        for(int j=0;j<si;j++){
            seki /= 27;
            score += alpha[s[i][j]]*seki;
        }
        a.emplace_back(make_pair(score,i));
    }
    sort(all(a));
    rep(i,n){
        cout<<s[a[i].second]<<endl;
    }
}
