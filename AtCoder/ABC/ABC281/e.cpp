#include <bits/stdc++.h>
#include <atcoder/all>
#include <time.h>

using namespace atcoder;
using namespace std;
#define _GLIBCXX_DEBUG

using ll = long long;
using pii = pair<int, int>;
using Pll = pair<long long, long long>;
using vec = vector<int>;
using vecll = vector<long long>;
using Graph = vector<vector<int>>;
using Graphll = vector<vector<long long>>;
using mat = vector<vector<int>>;
using matll = vector<vector<long long>>;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define rep2(i, m, n) for (ll i = (ll)(m); i < (ll)(n); i++)

#define forall(i, v) for (auto& i : v)
#define forallpair(i, j, v) for (auto& [i, j] : v)

#define all(v) v.begin(), v.end()
#define YesNo(a) ((a) ? "Yes" : "No")
#define YESNO(a) ((a) ? "YES" : "NO")
#define yesno(a) ((a) ? "yes" : "no")

// using mod = modint1000000007;
// using mod = modint998244353;
#define __SPEED_UP__                  \
    ios_base::sync_with_stdio(false); \
    cin.tie(nullptr);


constexpr int MOD = 1000000007;
const long long INF = 1LL << 60;
const int inf = 1<<30;

template <typename T>
T gcd(T a, T b) { return b ? gcd(b, a % b) : a; }
template <typename T>
T lcm(T a, T b) { return a / gcd(a, b) * b; }

template <typename T>
long long sum(vector<T> v){
	ll Sum = 0;
	for(int i = 0;i<v.size();i++) Sum += v[i];
	return Sum;}
double sum(vector<double> v){
	double Sum = 0;
	for(int i = 0;i<v.size();i++)  Sum += v[i];
	return Sum;}
double Min(vector<double> v){
	double ans = v[0];
	for(int i = 0;i<v.size();i++) ans = min(ans,v[i]);
	return ans;}
double Max(vector<double> v){
	double ans = v[0];
	for(int i = 0;i<v.size();i++) ans = max(ans,v[i]);
	return ans;}
int Min(vector<int> v){
	int ans = v[0];
	for(int i = 0;i<v.size();i++) ans = min(ans,v[i]);
	return ans;}
int Max(vector<int> v){
	int ans = v[0];
	for(int i = 0;i<v.size();i++) ans = max(ans,v[i]);
	return ans;}
long long Min(vector<long long> v){
	long long ans = v[0];
	for(int i = 0;i<v.size();i++) ans = min(ans,v[i]);
	return ans;}
long long Max(vector<long long> v){
	long long ans = v[0];
	for(int i = 0;i<v.size();i++) ans = max(ans,v[i]);
	return ans;}

struct multiset_sum{
    ll low_sum, high_sum, partition;
    multiset<ll> low_st, high_st;
 
    multiset_sum(){low_sum = high_sum = partition = 0;}
    int size(){return (int)low_st.size() + (int)high_st.size();}
    void insert(ll x){
        if(high_st.size() && *high_st.begin() <= x)high_st.insert(x),high_sum += x;
        else low_st.insert(x),low_sum += x;
        adjust();
    }
    void erase(ll x){
        if(high_st.size() && *high_st.begin() <= x)high_st.erase(high_st.find(x)),high_sum -= x;
        else low_st.erase(low_st.find(x)),low_sum -= x;
        adjust();
    }
    void adjust(){
        while((int)low_st.size() > partition){
            int low_mx = *low_st.rbegin();
            high_sum += low_mx;
            low_sum -= low_mx;
            high_st.insert(low_mx);
            low_st.erase(low_st.find(low_mx));
        }
        while((int)low_st.size() < partition && high_st.size()){
            int high_mn = *high_st.begin();
            low_sum += high_mn;
            high_sum -= high_mn;
            low_st.insert(high_mn);
            high_st.erase(high_st.find(high_mn));
        }
    }
    void adjust(ll x){
        partition = x;
        adjust();
    }
    ll get_lowsum(int k){
        //小さい方からk個の和
        if(k<0)return 0;
        if(k>=size())return low_sum+high_sum;
        adjust(k);
        return low_sum;
    }
    ll get_highsum(int k){
        //大きい方からk個の和
        if(k<0)return 0;
        if(k>=size())return low_sum+high_sum;
        int lk = size()-k;
        adjust(lk);
        return high_sum;
    }
};


int main() {
	__SPEED_UP__
	int n,m,k;
	cin>>n>>m>>k;
	vec a(n);
	rep(i,n)cin>>a[i];
	multiset_sum st;
	rep(i,m){
		st.insert(a[i]);
	}
	cout<<st.get_lowsum(k)<<' ';
	for(int i = m;i<n;i++){
		st.erase(a[i-m]);
		st.insert(a[i]);
		cout<<st.get_lowsum(k)<<' ';
	}

	
}
