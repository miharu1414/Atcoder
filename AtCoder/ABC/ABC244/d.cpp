
#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using pii = pair<int, int>;
using Pll = pair<long long,long long>;
using vec = vector<int>;
using vecll = vector<long long>;
using mat = vector<vector<int>>;
using matll = vector<vector<long long>>;
#define rep(i, n) for(int i = 0; i < (int)(n); i++)
#define all(v) v.begin(), v.end()
#define endl "\n"
#define _GLIBCXX_DEBUG
#define absolute(a) max(a,-a)

constexpr int MOD = 1000000007;
const int INF = 1 << 30;

template<typename T> T gcd(T a, T b) { return b ? gcd(b, a%b) : a; }
template<typename T> T lcm(T a, T b) { return a / gcd(a, b) * b ;}


char change_int(char x){
    if(x=='R') return '1';
    else if (x=='G') return '2';
    else return '3';
}


int main(){
    vector<char> s(3),t(3);
    string S;
    string T;
    vector<string> koho1 = {"123","312","231"};
    vector<string> koho2= {"213","132","321"};
    rep(i,3){
        cin>>s[i];
        
        S += change_int(s[i]);
    }
    rep(i,3){
        cin>>t[i];
        T += change_int(t[i]);
    }

    int which = 2;
    rep(i,3){
        if(koho1[i]==S) which = 1;
    }

    int ans = 2;
    rep(i,3){
        if(koho1[i]==T) ans = 1;
    }
    if(which==ans) cout<<"Yes"<<endl;
    else cout<<"No"<<endl;
    
    
}