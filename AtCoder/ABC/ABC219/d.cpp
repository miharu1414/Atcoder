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
    int n;
    cin>>n;
    int x,y;
    cin>>x>>y;
    vector<int> a(n),b(n);
    
    map<int,int> a_pos,b_pos;
      vector<int> oria(n),orib(n);
      vector<pair<int,int>> ab,ba;
      set<pair<int,int>> s;
      vector<tuple<int,int,int>> t;
    rep(i,n){
        cin>>a[i]>>b[i];
        ab.emplace_back(make_pair(a[i],b[i]));
        ba.emplace_back(make_pair(b[i],a[i]));
        int sum = a[i]+b[i];
        t.emplace_back(make_tuple(sum,a[i],b[i]));
        
    }
  
    sort(all(ab));
    sort(all(ba));
    int x_count = 0;
    int y_count = 0;
    int count = 0;
    bool okx = false;
    bool oky = false;


    rep(i,n){
        if(x_count>=x){
            okx = true;
            break;
        }
        else if(y_count>=y){
            oky = true;
            break;
        }
        x_count += get<1>(t[n-1-i]);
        y_count += get<2>(t[n-1-i]);
        s.insert(make_pair(get<1>(t[n-1-i]),get<2>(t[n-1-i])));
        count++;
    }
    rep(i,n){
        if(x_count>=x){
            okx = true;
            break;
        }

        if(s.count(make_pair(ab[n-1-i].first,ab[n-1-i].second))) continue;
        x_count += ab[n-1-i].first;
        count ++;
        y_count += ab[n-1-i].second;
        s.insert(make_pair(ab[n-1-i].second,ab[n-1-i].first));
        if(x_count>=x){
            okx = true;
            break;
        }
    }
    if(okx == false ){
        cout<<-1;
        return 0;
    }
    
    rep(i,n){
        if(y_count>=y){
            oky = true;
            break;
        }
        if(s.count(make_pair(ba[n-1-i].first,ba[n-1-i].second))) continue;
        y_count += ba[n-i-1].first;
        count++;
        if(y_count>=y){
            oky = true;
            break;
        }
    }
    if(oky==false){
        cout<<-1;
        return 0;
    }
    cout<<count<<endl;

}
