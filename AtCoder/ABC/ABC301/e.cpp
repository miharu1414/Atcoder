#include <iostream>
#include <vector>
#include <deque>
#include <algorithm>
#include <climits>
using namespace std;

int dx[] = {1, 0, -1, 0};
int dy[] = {0, 1, 0, -1};

int bit_count(int number) {
    int count = 0;
    while (number) {
        count += number & 1;
        number >>= 1;
    }
    return count;
}

vector<vector<int>> bfs(const vector<string>& a, int sx, int sy) {
    int h = a.size();
    int w = a[0].size();
    vector<vector<int>> dist(h, vector<int>(w, -1));
    deque<pair<int, int>> d;

    dist[sx][sy] = 0;
    d.push_back({sx, sy});

    while (!d.empty()) {
        int x = d.front().first;
        int y = d.front().second;
        d.pop_front();

        for (int i = 0; i < 4; ++i) {
            int x2 = x + dx[i];
            int y2 = y + dy[i];
            if (x2 < 0 || x2 >= h || y2 < 0 || y2 >= w) {
                continue;
            }
            if (a[x2][y2] == '#') {
                continue;
            }
            if (dist[x2][y2] == -1) {
                dist[x2][y2] = dist[x][y] + 1;
                d.push_back({x2, y2});
            }
        }
    }

    return dist;
}

const long long INF = LLONG_MAX;

int main() {
    int h, w, t;
    cin >> h >> w >> t;
    vector<string> a(h);
    for (int i = 0; i < h; ++i) {
        cin >> a[i];
    }

    vector<pair<int, int>> nodes;
    int start = -1;
    int goal = -1;
    for (int i = 0; i < h; ++i) {
        for (int j = 0; j < w; ++j) {
            if (a[i][j] == 'S') {
                start = nodes.size();
                nodes.push_back({i, j});
            } else if (a[i][j] == 'G') {
                goal = nodes.size();
                nodes.push_back({i, j});
            } else if (a[i][j] == 'o') {
                nodes.push_back({i, j});
            }
        }
    }
    int n = nodes.size();

    vector<vector<long long>> G(n, vector<long long>(n, INF));
    for (int i = 0; i < n; ++i) {
        int x = nodes[i].first;
        int y = nodes[i].second;
        vector<vector<int>> dist = bfs(a, x, y);
        for (int j = 0; j < n; ++j) {
            int x2 = nodes[j].first;
            int y2 = nodes[j].second;
            if (dist[x2][y2] != -1) {
                G[i][j] = dist[x2][y2];
            }
        }
    }

    vector<vector<long long>> dp(1 << n, vector<long long>(n, INF));
    dp[1 << start][start] = 0;
	for (int bit = 1; bit < (1 << n); ++bit) {
        for (int v = 0; v < n; ++v) {
            for (int v2 = 0; v2 < n; ++v2) {
                int nbit = bit | (1 << v2);
                dp[nbit][v2] = min(dp[nbit][v2], dp[bit][v] + G[v][v2]);
            }
        }
    }

    int res = -1;
    for (int bit = 1; bit < (1 << n); ++bit) {
        if (dp[bit][goal] <= t) {
            res = max(res, bit_count(bit) - 2);
        }
    }
    cout << res << endl;

    return 0;
}