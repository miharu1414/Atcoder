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
    set<int> s;
    map<int,int> S;
    for(int i =0;i<n;i++){
        int a;
        cin>>a;
        int x;
        if (a==1){
            cin>>x;
            if(s.count(x)){
                S[x]++;
            }
            else{
                S[x] = 1;
                s.insert(x);
            }
        }
        else if(a==2){
            cin>>x;
            int c;
            cin>>c;
            if(s.count(x)){
                if(S[x]<=c){
                    S[x]=0;
                    s.erase(x);
                }
                else{
                    S[x] = S[x] - c;
                }
            }
        }
        else{
            cout<<*rbegin(s)-*begin(s)<<endl;
        }
    }

}