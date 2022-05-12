#include <bits/stdc++.h>
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
#define absolute(a) max(a, -a)

constexpr int MOD = 1000000007;
const int INF = 1 << 30;

template <typename T>
T gcd(T a, T b) { return b ? gcd(b, a % b) : a; }
template <typename T>
T lcm(T a, T b) { return a / gcd(a, b) * b; }

vector<int> a;
int tori(long long n){
  if(n == 0|| n == 1) return 0;
  else if(n == 2) return 1;
  else if (a[n] != -1) return a[n]%10007;
  return a[n] = (tori(n-1)+tori(n-2)+tori(n-3))% 10007;
}int main(){
  long long N;cin >> N;
 a.assign(N, -1);
  tori(N-1);
  if(a[N-1] != -1) cout << tori(N-1)<< endl;
  else if(N ==3) cout << 1 << endl;
  else cout<< 0 << endl;
 
}
