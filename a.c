#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>
#define M_PI 3.14159265358979323846264338327950288

double f(double x){
    double ans;
	ans = exp(-x*x/2)/sqrt(2*M_PI);
    return ans;
}
double Mean(int n, double y[]){
	double ave = 0;
	int i;
	for(i = 0;i<n;i++){
		ave += y[i];
	}
	return ave / n;
}

void summary(int num, double ans[]){
	int i;
	double answer, min, max;
	answer = Mean(num, ans);
	min = ans[0], max = ans[0];
	for(i = 1;i<num;i++){
		if(ans[i] > max) max = ans[i];
		else if(ans[i] < min) min = ans[i];
	}
	printf("%d回の実験結果の集計が終わりました．\n",num);
	printf("最終的な答え(平均値) ＝ %lf\n",answer);
	printf("ばらつき %lf～%lf\n",min,max);
}


void cal(int num, int n, double a, double ans[]){
	int i,j;
	double y[1000],X,t;
	for(i = 0;i<num;i++){
		for(j = 0;j < n;j++){
            y[j] = 1;
			X = a * sqrt(rand())/(sqrt(RAND_MAX)+1);
			t = f(X);
            y[j] = t;
		}
		ans[i] = 2 * Mean(n, y);
	printf("%d番目の演算結果は　%lf\n", i,ans[i]);
	}
}


		

int main(){
	int n,num;
	double a,ans[1000];
	srand(time(NULL)*12345);
	printf("実験回数：");
	scanf("%d", &num);
	printf("1回あたりの乱数の生成数：");
	scanf("%d", &n);
	printf("積分区間[-a,a]: a = ");
	scanf("%lf", &a);
	cal(num,n,a,ans);
	summary(num,ans);
	system("pause");
}

