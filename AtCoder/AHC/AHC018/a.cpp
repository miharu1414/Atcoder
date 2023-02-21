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



struct Pos {
	int y,x;
};

enum class Response {
	not_broken, broken, finish, invalid
};

struct Field {
	int N;
	int C;
	vector<vector<int>> is_broken;
	int total_cost;

	Field(int N, int C) : N(N), C(C), is_broken(N, vector<int>(N, 0)) {}
	
	Response query(int y, int x, int power){
		total_cost += power + C;
		cout << y << ' ' << x << ' ' << power << endl;
		int r;
		cin >> r;
		switch (r){
			case 0:
				return Response::not_broken;
			case 1:
				is_broken[y][x] = 1;
				return Response::broken;
			case 2:
				is_broken[y][x] = 1;
				return Response::finish;
			default:
				return Response::invalid;

		}
	}
};

struct Solver {
	int N, C;
	vector<Pos> source_pos, house_pos;
	Field field;
	
	Solver(int N, const vector<Pos>& source_pos, const vector<Pos> &house_pos,int C):
		N(N),source_pos(source_pos), house_pos(house_pos), C(C), field(N,C) {

	}

	void solve(){
		for (Pos house: house_pos){
			move(house, source_pos[0]);
		}
		        // should receive Response::finish and exit before entering here
        assert(false);
	}

	void move(Pos start, Pos goal){
		  // you can output comment
        cout << "# move from (" << start.y << "," << start.x << ") to (" << goal.y << "," << goal.x << ")" << endl;
	
        // down/up
        if (start.y < goal.y) {
            for (int y = start.y; y < goal.y; y++) {
                destruct(y, start.x);
            }
        } else {
            for (int y = start.y; y > goal.y; y--) {
                destruct(y, start.x);
            }
        }

        // right/left
        if (start.x < goal.x) {
            for (int x = start.x; x <= goal.x; x++) {
                destruct(goal.y, x);
            }
        } else {
            for (int x = start.x; x >= goal.x; x--) {
                destruct(goal.y, x);
            }
        }
    }

    void destruct(int y, int x) {
        // excavate (y, x) with fixed power until destruction
        const int power = 250;
        while (!field.is_broken[y][x]) {
            Response result = field.query(y, x, power);
            if (result == Response::finish) {
                cerr << "total_cost=" << field.total_cost << endl;
                exit(0);
            } else if (result == Response::invalid) {
                cerr << "invalid: y=" << y << " x=" << x << endl;
                exit(1);
            }
        }
    }
};
int main() {


    clock_t now= clock();


    clock_t start = clock();
    while(1){
        now = clock();
        double diff = (double)(now - start)/1000;

        if(diff>4800){
            break;
            cout<<1<<endl;
        }
    }

    
	
}
