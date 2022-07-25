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
T gcd(T a, T b) { return b ? gcd(b, a % b) : a; }
template <typename T>
T lcm(T a, T b) { return a / gcd(a, b) * b; }


int sum(vector<int> v){
	int sum = 0;
	for(int i = 0;i<v.size();i++) sum += v[i];
	return sum;
}
double sum(vector<double> v){
	double sum = 0;
	for(int i = 0;i<v.size();i++)  sum += v[i];
	return sum;
}






int main() {

	ll n,x ; cin>>n>>x;
    string s;
    cin>>s;
    for(int i = 0;i<n;i++){
        if(s[i]=='U'){

        }
        else if(s[i]=='R'){

        }
        else{
            
        }

    }


}