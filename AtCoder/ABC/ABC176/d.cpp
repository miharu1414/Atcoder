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



// マスを表すデータ構造
using Node = pair<int,int>;

// 四方向への移動を表すベクトル
// 0: 下、1: 右、2: 上、3: 左
vector<int> dx = {1, 0, -1, 0};
vector<int> dy = {0, 1, 0, -1};

vector<int> dx1 = {0,2,0,-2,1,-1,1,-1,2,2,2,2,-2,-2,-2,-2,1,-1,1,-1};
vector<int> dy1 = {2,0,-2,0,1,1,-1,-1,1,-1,2,-2,1,-1,2,-2,2,2,-2,-2};

int main() {
	__SPEED_UP__
	// 入力
	int H, W, sy,sx,gy,gx;
    cin >> H >> W >> sy >> sx >> gy >> gx;
	sy--;
	sx--;
	gy--;
	gx--;
    vector<string> S(H);
    for (int i = 0; i < H; ++i) cin >> S[i];
    
    // 各マス (x, y) が何手目に探索されたか
    // -1 は「まだ探索されていない」ことを表す
    vector<vector<int>> dist(H, vector<int>(W, -1));

    // todo リストを表すキュー
    queue<Node> que;

    // マス (X0, Y0) を始点とする
    dist[gy][gx] = 0;
    que.push(Node(gy, gx));

    // キューが空になるまで探索する
    while (!que.empty()) {
        // キューから頂点を取り出す
        auto [y, x] = que.front();
        que.pop();
        
        // マス (x, y) から 1 手で行けるマスを順に探索
        for (int direction = 0; direction < 4; ++direction) {
            // 隣接マス
            int x2 = x + dx[direction];
            int y2 = y + dy[direction];

			if(W>x2 && x2>=0 && H>y2 && y2>=0 && S[y2][x2] =='.' && (dist[y2][x2] == -1 || dist[y2][x2] > dist[y][x] ) ){
				dist[y2][x2] = dist[y][x] ;
        		que.push(Node(y2, x2));
			}
        }

		 // マス (x, y) から 1 手で行けるマスを順に探索
        for (int direction = 0; direction < 20; ++direction) {
            // 隣接マス
            int x2 = x + dx1[direction];
            int y2 = y + dy1[direction];

			if(W>x2 && x2>=0 && H>y2 && y2>=0 && S[y2][x2] =='.' && (dist[y2][x2] == -1 || dist[y2][x2] > dist[y][x] + 1) ){
				dist[y2][x2] = dist[y][x]+1 ;
        		que.push(Node(y2, x2));
			}
        }
    }

    // マス (X1, Y1) の値を答える
    cout << dist[sy][sx] << endl;
}
	
	

