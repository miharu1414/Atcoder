#include <bits/stdc++.h>     
#include <iostream>
#include <string>
#include <stdexcept>

using namespace std;
using ll = long long;
using pii = pair<int, int>;
using pll = pair<long long,long long>;
using vec = vector<int>;
using vecll = vector<long long>;
using mat = vector<vector<int>>;
using matll = vector<vector<long long>>;
#define rep(i, n) for(int i = 0; i < (int)(n); i++)
#define all(v) v.begin(), v.end()
#define endl "\n"
#define _GLIBCXX_DEBUG
constexpr int MOD = 1000000007;
const int INF = 1 << 30;
template<typename T> T gcd(T a, T b) { return b ? gcd(b, a%b) : a; }
template<typename T> T lcm(T a, T b) { return a / gcd(a, b) * b ;}
int main(){
    int k;
    cin>>k;
    string a,b;
    cin>>a>>b;
    vector<int> sinsuu;

    rep(i,k){
        sinsuu.push_back(i);
    }
    ll ansa=0,ansb=0;
    int sizea = a.size();
    int sizeb= b.size();
    ll memo =1;
    rep(i,sizea){
        if(i==0) ansa += a[sizea-i-1]-'0';
        else{
            memo *= k;
            ansa +=  (a[sizea-i-1]-'0')*memo;
        }
    }
    memo =1;
    rep(i,sizeb){
        if(i==0) ansb += b[sizeb-1-i]-'0';
        else{
            memo *= k;
            ansb +=  (b[sizeb-1-i]-'0')*memo;
        }
    }
    cout<<ansa*ansb<<endl;

}