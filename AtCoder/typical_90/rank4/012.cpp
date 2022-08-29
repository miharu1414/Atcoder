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





struct UnionFind {
    vector<int> par; // par[i]:iの親の番号　(例) par[3] = 2 : 3の親が2

    UnionFind(int N) : par(N) { //最初は全てが根であるとして初期化
        for(int i = 0; i < N; i++) par[i] = i;
    }

    int root(int x) { // データxが属する木の根を再帰で得る：root(x) = {xの木の根}
        if (par[x] == x) return x;
        return par[x] = root(par[x]);
    }

    void unite(int x, int y) { // xとyの木を併合
        int rx = root(x); //xの根をrx
        int ry = root(y); //yの根をry
        if (rx == ry) return; //xとyの根が同じ(=同じ木にある)時はそのまま
        par[rx] = ry; //xとyの根が同じでない(=同じ木にない)時：xの根rxをyの根ryにつける
    }

    bool same(int x, int y) { // 2つのデータx, yが属する木が同じならtrueを返す
        int rx = root(x);
        int ry = root(y);
        return rx == ry;
    }
};




int h,w;
int T(int x,int y){
    return w*x + y;
}




int dx[] = {1,-1,0,0};
int dy[] = {0,0,1,-1};
int main() {


    cin>>h>>w;
    int q;
    cin>>q;
    mat masu(h,vector<int> (w,0));



    UnionFind uf(h*w);


    rep(i,q){
        int x;cin>>x;

        if(x==1){
            int r,c;
            cin>>r>>c;
            r--;
            c--;
            masu[r][c] = 1;

            rep(j,4){
                int now_x = r + dx[j];
                int now_y = c +dy[j];

                if(now_x >= h || now_x < 0 || now_y >= w || now_y < 0) continue;
                if(masu[now_x][now_y] & masu[r][c]) uf.unite(T(now_x,now_y),T(r,c));
            }

        }

        else{
            int ra,ca,rb,cb;
            cin>>ra>>ca>>rb>>cb;
            ra--;ca--;rb--;cb--;
            if((masu[ra][ca] & masu[rb][cb]) && (uf.same(T(ra,ca),T(rb,cb)))){
                cout<<"Yes"<<endl;
            }
            else{
                cout<<"No"<<endl;
            }
        }


        }
    
}