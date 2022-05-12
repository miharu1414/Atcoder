#include <bits/stdc++.h>
#include <atcoder/all>

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

int shiki(int*, int, int);

int main(){
	int n,m;
    cin>>n>>m;
    vector<int> avec(n+1), cvec(n+m+1);
    rep(i,n+1) cin>>avec[n-i];
    rep(i,n+m+1) cin>>cvec[n+m-i];
	int a = 0, b = 0, i, j;
	

			
			a= m+n;
			if( cin.fail() ){
				throw 1;
			}
			int *A;
			A = new int[a+1];
			
			for (i=0; i<=a; i++){
			
				if (a-i==1){
				
				}else if (a-i>1){
					
				}
				if (i<a){
					
				}
			}

		
			
			for (i=0; i<=a; i++){
			
				A[i] = cvec[i];
				if( cin.fail() ){
					throw 1;
				}
			}

			b = n;
			if( cin.fail() ){
				throw 1;
			}
			int *B;
			B = new int [b+1];

			for (i=0; i<=b; i++){
			
				if (b-i==1){
					
				}else if (b-i>1){
					
				}
				if (i<b) {
					
				}
			}
			
	
			
			for (i=0; i<=b; i++){
				
				B[i] = avec[i];
				if( cin.fail() ){
					throw 1;
				}
			}



			int *Q ,*R;
			Q = new int[a-b+1];
			R = new int[a+1];
			for (i=0; i<=a; i++) {
				R[i] = A[i];
			}
			for (i=0; i<=a-b; i++){
				Q[i] = R[i] / B[0];
				for (j=0; j<=b; j++){
					int k = i + j;
					R[k] -= Q[i]*B[j];
				}
			}
			
			shiki (Q, a-b,m);

		

	

	return 0;
}

int shiki (int x[], int y,int m){
	int i,j;
    vector<int> ans(m+1);
	for (i=0 ; i<=y ; i++){
		if (x[i] > 0 || x[i] < 0){
			j=i;
			break;
		}
	}
    int k = 0;
	for (i=j ; i<=y ; i++){
		if (x[i] > 0 && i>j){
			
		}
		if (x[i] != 0 && y-i==1){
			if (x[i] != 1 && x[i] != -1){
			ans[k] = x[i];k++;
			}else if (x[i] == -1){
			ans[k] = x[i];k++;
			}
			
		}else if (x[i] != 0 && y-i>1){
			if (x[i] != 1 && x[i] != -1){
			ans[k] = x[i];k++;
			}else if (x[i] == -1){
			ans[k] = x[i];
            k++;
			}
			
		}else if (x[i] != 0){
			ans[k] = x[i];k++;
		}
	}
    rep(i,m+1) cout<<ans[m-i]<<" ";
	return 0;
}