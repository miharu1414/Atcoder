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


template <typename T>
T  sum(vector<T> v){
	int sum = 0;
	for(int i = 0;i<v.size();i++) sum += v[i];
	return sum;
}






int n;





int main() {
    int q, num, x,y;
    cin>>n>>q;

    vector<vector<int>> train(n+1,vector<int>(2,-1));

    for(int i = 0;i<q;i++){
        cin>>num;
        if(num == 1){
            cin>>x>>y;
            train[x][1] = y;
            train[y][0] = x;
        }
        else if(num ==2){
            cin>>x>>y;
            train[x][1] = -1;
            train[y][0] = -1;

        }
        else{
            cin>>x;
            int cnt = 1,now = x;
            while(train[now][1] != -1){
                now = train[now][1];
            }
            while(train[now][0] != -1){
                now = train[now][0];
                cnt += 1;
            }

            
            cout<<cnt<<" "<<now<<" ";
            while(train[now][1] != -1){
                cout<<train[now][1]<<" ";
                now = train[now][1];
            }
            cout<<endl;
        }
    }




}