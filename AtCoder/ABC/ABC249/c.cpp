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
     int n,k;
     cin>>n>>k;
     vector<string> s(n);
     rep(i,n) cin>>s[i];
     int ans = 0;

    // {0, 1, ..., n-1} の部分集合の全探索
    for (int bit = 0; bit < (1<<n); ++bit) {
        vector<int> S;
        vector<int> count(26,0);
        for (int i = 0; i < n; ++i) {
            if (bit & (1<<i)) { // 列挙に i が含まれるか
                S.push_back(i);
            }
        }


        for (int i = 0; i < (int)S.size(); ++i) {
            string target = s[S[i]];
            for(int j = 0;j<target.size();j++){
                count[target[j]-'a']++;
            }
            int num = 0;
        for(int j = 0;j<26;j++){
            if(count[j]==k) num++;
                       } 
        ans = max(ans,num);   
            
        }
     
    }
    cout<<ans<<endl;

}