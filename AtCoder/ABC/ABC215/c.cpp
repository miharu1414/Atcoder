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
#define DO_TEST(exp)    do_test(exp, __LINE__)
void do_test(bool b, int line) {
    if( b ) return;     //  OK
    cout << "\nNG at line " << line << "\n";
    exit(1);
}
void my_sort(vector<string>& lst) {
    //  ToDo: 標準ライブラリの関数を使い、lst の要素を昇順ソートする
}
int main(){
    string s;
    cin>>s;
    int k;
    cin>>k;
    vector<string> z;
    int len = s.size();
    vec index(len);
    rep(i,len) index[i]=i;
    int j =0;
    set<string> zdou;
    do{
        string za="";
        for(int i =0;i<len;i++){
            char x = s[index[i]];
            za = za +x;
        }
        if(zdou.count(za));
        else{
            zdou.insert(za);
            z.emplace_back(za);
        }
        j++;
    }while(next_permutation(index.begin(),index.end()));
    sort(all(z));
    cout<<z[k-1]<<endl;
}

   