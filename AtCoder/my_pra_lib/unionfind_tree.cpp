#include <iostream>
#include <vector>
using namespace std;


//https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_1_A&lang=jp の問題

struct UnionFind{
    vector<int> p;
    UnionFind(int n){
        p.resize(n, -1);
    }
    int find(int x){ 
        if(p[x] == -1) return x;
        else return p[x] =  find(p[x]);
    }

    void unite(int x, int y){
        x = find(x);
        y = find(y);
        if(x==y) return;
        p[x] = y;
    }
};

int main() {
    int n,q,com,x,y;
    cin >> n >> q;
    UnionFind uf(n);
    for(int i = 0; i < q;i++){

        if (com == 0){
            uf.unite(x,y);
        }
        else{
            if(uf.find(x)==uf.find(y)){
                cout<<1<<endl;
            }
            else cout<<0<<endl;
        }
    }
}