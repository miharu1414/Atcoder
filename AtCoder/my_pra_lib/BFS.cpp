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

int main(){
    int n, q;//頂点数と辺の数
    cin >> n >> q;   

    //グラフ入力受け取り
    vector<vector<int>> G(n);
    for (int i = 0; i < q;i++){
        int a, b;
        cin>>a>>b;
        G[a].emplace_back(b);
        G[b].emplace_back(a);
    }
    //BFSのためのデータ構造
    vector<int> dist(n, -1); //全頂点を「未訪問」に初期化
    queue<int> que;

    //初期条件（頂点を初期ノードとする）
    dist[0] = 0;
    que.push(0);//0を橙色頂点とする

    //BFS開始（キューが空になるまで探索を行う）
    while(!que.empty()){
        int v = que.front();//キューから先頭頂点を取り出す
        que.pop();
    //vから訪れる頂点を全て調べる
        for(int nv:G[v]){
            if(dist[nv] != -1)continue;

            //新たな白色頂点nvについて距離情報を更新してキューに追加する
            dist[nv] = dist[v] + 1;
            que.push(nv);

        }
    }
     // 結果出力 (各頂点の頂点 0 からの距離を見る)
    for (int v = 0; v < n; ++v) cout << v << ": " << dist[v] << endl;
}
    