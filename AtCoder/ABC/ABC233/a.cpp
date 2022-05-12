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
<<<<<<< HEAD:ABC/ABC233/a.cpp
     int x,y,ans;
     cin>>x>>y;
     ans = 0;
     while(x<y){
         ans +=1;
         x += 10;
     }
     cout<<ans<<endl;
}
=======
//練習問題４－５

	int a,b,c;
	cin>>a>>b>>c;
	cout<<gcd(gcd(a,b),c)<<endl;

}


	
>>>>>>> 497d17464be8ef8a549f44aff5ac55831b086c35:test.cpp
