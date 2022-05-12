#include <bits/stdc++.h>
  #include <time.h>
    
using namespace std;

bool hantei(string S) {
	int dep = 0;
	for (int i = 0; i < S.size(); i++) {
		if (S[i] == '(') dep += 1;
		if (S[i] == ')') dep -= 1;
		if (dep < 0) return false;
	}
	if (dep == 0) return true;
	return false;
}

int main() {
    clock_t start = clock();
	int N;
	cin >> N;
	for (int i = 0; i < (1 << N); i++) {
		string Candidate = "";
		for (int j = N - 1; j >= 0; j--) {
			// メモ : (i & (1 << j)) = 0 というのは、i の j ビット目（2^j の位）が 0 であるための条件。
			// 　　　頻出なので知っておくようにしましょう。
			if ((i & (1 << j)) == 0) {
				Candidate += "(";
			}
			else {
				Candidate += ")";
			}
		}
		bool I = hantei(Candidate);
		if (I == true) cout << Candidate << endl;
	}
	


     // 何かの処理

    clock_t end = clock();

    const double time = static_cast<double>(end - start) / CLOCKS_PER_SEC * 1000.0;
    printf("time %lf[ms]\n", time);

    return 0;
}