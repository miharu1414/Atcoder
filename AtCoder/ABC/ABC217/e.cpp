#include <atcoder/all>
#include <bits/stdc++.h>
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
#define rep(i, n) for(int i = 0; i < (int)(n); i++)
#define all(v) v.begin(), v.end()
#define endl "\n"
#define _GLIBCXX_DEBUG

constexpr int MOD = 1000000007;
const int INF = 1 << 30;

template <typename T> T gcd(T a, T b) { return b ? gcd(b, a % b) : a; }
template <typename T> T lcm(T a, T b) { return a / gcd(a, b) * b; }

int main() {
    int n;
    cin >> n;
    queue<int> std;
    priority_queue<int, vector<int>, greater<int>> pq;

    rep(i, n) {
        int q;
        cin >> q;

        if(q == 1) {
            int x;
            cin >> x;
            std.push(x);

        } else if(q == 2) {
            if(pq.empty()) {
                cout << std.front() << endl;
                std.pop();
            } else {
                cout << pq.top() << endl;
                pq.pop();
            }

        } else {
            while(!std.empty()){
                pq.push(std.front());
                std.pop();
            }
        }
    }
}