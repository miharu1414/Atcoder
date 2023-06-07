#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    int w, h;
    std::cin >> w >> h;

    int n;
    std::cin >> n;

    std::vector<int> p(n), q(n);
    for (int i = 0; i < n; i++) {
        std::cin >> p[i] >> q[i];
    }

    int A;
    std::cin >> A;
    std::vector<int> a(A);
    for (int i = 0; i < A; i++) {
        std::cin >> a[i];
    }

    int B;
    std::cin >> B;
    std::vector<int> b(B);
    for (int i = 0; i < B; i++) {
        std::cin >> b[i];
    }

    std::vector<std::vector<int>> group(A + 1, std::vector<int>(B + 1, 0));
    for (int i = 0; i < n; i++) {
        int former = std::lower_bound(a.begin(), a.end(), p[i]) - a.begin();
        int latter = std::lower_bound(b.begin(), b.end(), q[i]) - b.begin();
        group[former][latter] += 1;
    }

    int min_value = 100000000;
    int max_value = -10000000;
    for (int i = 0; i <= A; i++) {
        for (int j = 0; j <= B; j++) {
            if (group[i][j] < min_value) {
                min_value = group[i][j];
            }
            if (group[i][j] > max_value) {
                max_value = group[i][j];
            }
        }
    }

    std::cout << min_value << " " << max_value << std::endl;

    return 0;
}
