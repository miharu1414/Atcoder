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
T gcd(T *it, T b) { return b ? gcd(b, *it % b) : *it; }
template <typename T>
T lcm(T *it, T b) { return *it / gcd(*it, b) * b; }





//以下、素集合と木は同じものを表す
class UnionFind{
public:
    vector<ll> parent; //parent[i]はiの親
    vector<ll> siz; //素集合のサイズを表す配列(1で初期化)
    map<ll,vector<ll>> group; //集合ごとに管理する(key:集合の代表元、value:集合の要素の配列)
    ll n; //要素数

    //コンストラクタ
    UnionFind(ll n_):n(n_),parent(n_),siz(n_,1){ 
        //全ての要素の根が自身であるとして初期化
        for(ll i=0;i<n;i++){parent[i]=i;}
    }

    //データxの属する木の根を取得(経路圧縮も行う)
    ll root(ll x){
        if(parent[x]==x) return x;
        return parent[x]=root(parent[x]);//代入式の値は代入した変数の値なので、経路圧縮できる
    }

    //xとyの木を併合
    void unite(ll x,ll y){
        ll rx=root(x);//xの根
        ll ry=root(y);//yの根
        if(rx==ry) return;//同じ木にある時
        //小さい集合を大きい集合へと併合(ry→rxへ併合)
        if(siz[rx]<siz[ry]) swap(rx,ry);
        siz[rx]+=siz[ry];
        parent[ry]=rx;//xとyが同じ木にない時はyの根ryをxの根rxにつける
    }

    //xとyが属する木が同じかを判定
    bool same(ll x,ll y){
        ll rx=root(x);
        ll ry=root(y);
        return rx==ry;
    }

    //xの素集合のサイズを取得
    ll size(ll x){
        return siz[root(x)];
    }



};


int main() {
    ll n,k;
    cin>>n>>k;
    vecll p(n);
    rep(i,n){
        int x;cin>>x;
        p[i] = x-1;
    }
    set<int> s;
    vecll ans(n,-1);
    vecll pre(n);

    if(k==1){
        rep(i,n) cout<<i+1<<endl;
        return 0;
    }

    UnionFind uf(n);
    for (int i = 0;i<n;i++){
        ll now = p[i];
        auto it = s.lower_bound(now);

        if(it == s.end()) s.insert(now);
        
        else{
            uf.unite(*it,now);
            pre[now] = *it; 
            s.erase(*it);
            s.insert(now);
        }

        if(uf.size(now) == k){
                s.erase(*it);
                ans[now] = i;
                for(ll j = 0;j<uf.size(now)-1;j++){
                    ans[pre[now]] = i;
                    now = pre[now];
                }

        }

    }   
    rep(i,n){ 
        if (ans[i]==-1) cout<<-1<<endl;
        else         cout<<ans[i]+1<<endl;
    }


}