#include <bits/stdc++.h>     
using namespace std;
using ll = long long;
using pii = pair<int, int>;
using pll = pair<long long,long long>;
using vec = vector<int>;
using vecll = vector<long long>;
using mat = vector<vector<int>>;
using matll = vector<vector<long long>>;
#define rep(i, n) for(int i = 0; i < (int)(n); i++)
#define all(v) v.begin(), v.end()
#define endl "\n"
#define _GLIBCXX_DEBUG
 
 constexpr int MOD = 1000000007;
 const int INF = 1 << 30;
   
   template<typename T> T gcd(T a, T b) { return b ? gcd(b, a%b) : a; }
   template<typename T> T lcm(T a, T b) { return a / gcd(a, b) * b ;}
   int main(){
       int n;
       cin >> n;
    vector<vector<int>> G(n);
    for (int i = 0; i < n-1;i++){
        int a, b;
        cin>>a>>b;
        G[a].emplace_back(b);
        G[b].emplace_back(a);
    }
    rep(i,n){
        sort(all(G[i]));
    }
        //BFSのためのデータ構造
    vector<int> dist(n, -1); //全頂点を「未訪問」に初期化
    stack<int> que;

    //初期条件（頂点を初期ノードとする）
    dist[0] = 0;
    que.push(0);//0を橙色頂点とする

    //BFS開始（キューが空になるまで探索を行う）
    while(!que.empty()){
        int v = que.top();//キューから先頭頂点を取り出す
    //vから訪れる頂点を全て調べる
                bool douda = true;
        for(auto nv:G[v]){

            if (dist[nv] != -1){
                cout << nv << " ";
                que.push(nv);
                douda = false;
            } 
        }
        if(douda){
            que.pop();
            cout << que.top()<<"";
        }
    }
   }