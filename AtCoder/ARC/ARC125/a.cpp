#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using pii = pair<int, int>;
using pll = pair<long long, long long>;
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
template <typename T> T gcd(T a, T b) { return b ? gcd(b, a % b) : a; }
template <typename T> T lcm(T a, T b) { return a / gcd(a, b) * b; }
int main() {
    int n, m;
    cin >> n >> m;
    vector<int> s(n),t(m);
    set<int> s_set,t_set;
    rep(i,n){
        cin>>s[i];
        s_set.insert(s[i]);
    }
    rep(i,m){
        cin>>t[i];
        t_set.insert(t[i]);
    }
    if(s_set.count(0)!=t_set.count(0)||s_set.count(1)!=t_set.count(1)){
        cout<<-1<<endl;
        return 0;
    }
    bool nok = true;
    int mnow =m-1;
    int count =0;
    int dif=1;
    if(s[0]==0){
        dif = 0;
    }
    int count_r=0,count_l=0,j=0,i=0;

    while(s[i]==dif){
        count_r++;
        i++;
        if(i==n) break;
    }
    while(s[j]==dif){
        count_l++;
        j--;
        if(j==-1) j =n-1;
        if(j==0) break;
    }
    ll min_count = min(count_l,count_r) ;
    int ans =0;
    bool nidou = true;
    int mae = s[0];
    while(nok){
        if(t[mnow]==mae){
                ans++;
        }
        else{
            if(nidou){
                ans += min_count+1;
                nidou = false;
            }
            else{
                ans +=2;

            }
            if(mae==1) mae = 0;
            else mae = 1;
        }
        
        mnow -=1;
        if(mnow==-1) break;
    }
    cout<<ans<<endl;


}