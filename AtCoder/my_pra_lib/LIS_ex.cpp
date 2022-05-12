#include <bits/stdc++.h>
#include <atcoder/all>
#include <time.h>

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

template <typename T>
int LIS(vector<T> a,vector<long long> &dp, int N){
    for(int i =0;i < N;i++){
        //dp[k] >= a[i]となる最小のイテレーター≒kを見つける
        auto it = lower_bound(dp.begin(), dp.end(), a[i]);
        //a[i]で置き換える
        *it = a[i];
    }
    return lower_bound(dp.begin(), dp.end(), INF) - dp.begin();//最長増加部分列の長さを返す
}

int main() {
    
    vector<int> ans;
    int size =0;
    printf("最長増加部分列を出力します\n配列を入力してください．　　　入力が終わったらquitと記述してください\n");
    while(true){
        string c;
        cin>>c;
        if( c.find("quit")==std::string::npos ) {  // quitがない場合の処理
        int n =stoi(c);
        ans.push_back(n);
        size++;
        }
        else break;
        }
        vector<int> lis(size);
        int N = size;
        vector<long long> dp(N, INF);
        while(size--){
            lis[size]=ans[size];
        }
        int s =LIS(lis,dp,N);
        for(int i =0;i<s;i++){
            cout<<dp[i]<<" ";
        }
        cout<<"最長単調増加部分列の長さは："<<s<<endl;
        

}