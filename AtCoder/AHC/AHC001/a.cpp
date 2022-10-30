#include <bits/stdc++.h>
#include <atcoder/all>
#include <time.h>

using namespace atcoder;
using namespace std;
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
#define all(v) v.begin(), v.end()

#define _GLIBCXX_DEBUG
clock_t start = clock();

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

void yesno(int x){cout<<(x==1?"yes":"no" )<<endl;}
void YesNo(int x){cout<<(x==1?"Yes":"No" )<<endl;}


      // 何かの処理


int dx[] = {1,-1,0,0};
int dy[] = {0,0,1,-1};


#include <random>
class Udrl{
    public:
        int up,down,right,left;
    public:
        int menseki(){
        return (up-down) * (right - left);
    }

};







Udrl udrl[200];
int n;

bool possible(int x){
    int u = udrl[x].up;
    int d = udrl[x].down;
    int r = udrl[x].right;
    int l = udrl[x].left;
    
    

    for(int i =0;i<n;i++){
        if(i==x) continue;
        int u1 = udrl[i].up;
        int d1 = udrl[i].down;
        int r1 = udrl[i].right;
        int l1 = udrl[i].left;

        if(u > u1 and d <= u1  and !(r < l1 or l > r1)) return false;
        if(u > d1 and d <= d1 and !(r < l1 or l > r1)) return false;
        if(r > l1 and l <= l1 and !(u < d1 or d > u1)) return false;
        if(r > r1 and l <= r1 and !(u < d1 or d > u1)) return false;
    }
    return true;
    
}



int main() {

    srand( time(NULL) );
    cin>>n;
    vector<int> X(n),Y(n),r(n);
    int x,y,nx,ny;
    rep(i,n) cin>>X[i]>>Y[i]>>r[i];

    //長方形の情報を格納

    rep(i,n){
        udrl[i].up = Y[i];
        udrl[i].down = Y[i] + 1;
        udrl[i].right = X[i]+1;
        udrl[i].left = X[i];
    }

    int cnt = 0;
    clock_t now= clock();
    while(1){
        now = clock();
        double diff = (double)(now - start);

        if(diff>4800){
            break;
            cout<<1<<endl;
        }
        ll now = rand()%n;
        int rd = rand()%4;

        if(rd==0){
            if (udrl[now].up != 0){            
                udrl[now].up -= 1;
                if(!possible(now)) udrl[now].up += 1;

            }



        }
        else if(rd==1){
            if(udrl[now].right != 9999){ 
                udrl[now].right += 1;
                if(!possible(now)) udrl[now].right -= 1;

            }
        }
        else if(rd == 2){
            if(udrl[now].down != 9999){
                udrl[now].down += 1;
                if(!possible(now)) udrl[now].down -= 1;

            }
        }
        else{
            if(udrl[now].left!=0){
                udrl[now].left -= 1;
                if(!possible(now)) udrl[now].left += 1;

            }
        }



        
        
    
    }
    rep(i,n) cout<<udrl[i].left<<" "<<udrl[i].up<<" "<<udrl[i].right<<" "<<udrl[i].down<<endl;






    
	
}
