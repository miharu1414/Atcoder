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
    string s3,s2,s1,t;
    cin>>s1>>s2>>s3>>t;
    string ans = "";
    for(auto x : t){
        if(x=='1'){
            cout<<s1;
        }
        else if(x=='2'){
            cout<<s2;
        }
        else{
            cout<<s3;
        }
    }
}