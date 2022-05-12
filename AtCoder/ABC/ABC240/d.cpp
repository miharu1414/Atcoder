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
    int n;
    cin>>n;
    vec a(n);rep(i,n) cin>>a[i];
    int erase_num = 0;
    int renzoku = 0;
    vec erase(n,0);
    vec Bool(n,1);
    cout<<1<<endl;
    int now = 0;

    for (int i =1;i<n;i++){
        if(i-renzoku<0) continue;
        renzoku = 1;
        int pos = 1;
        while(a[i]==a[i-pos]){
            while(Bool[i-pos]==0){
                pos ++;
            } 
            pos++;
            renzoku++;
        }
        if(renzoku==a[i]){
            erase_num += a[i];
            erase[i] += a[i];
            rep(j,renzoku) Bool[i-renzoku] = 0;
        }
        cout<<i+1-erase_num<<endl;
    }
}