#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

int main (){
	int point[1000],a[1000],num[1000],gakuseki[1000];

	int c,n,i,j,k,K,sum,count,temp;
	printf("学生は何人ですか:");
	scanf("%d",&n);
	printf("何グループに分けますか");
	scanf("%d",&K);
	for(i=0;i<n;i++){
		printf("%d番の生徒の成績",i+1);
		scanf("%d",&point[i]);
		gakuseki[i] = i;  //a[i] :学籍番号=iの人の点数   gakuseki[i] 点数が高い順に学籍番号が入っている
							//→　a[gakuseki[i]]，i番目に点数が高い人の点数
	}
	for(i=0;i<n;i++)a[i]=point[i];
	//成績降順バブルソート
	for(i=n-1;i>=1;i--){
		for(j=0;j<n-1;j++){
			if(point[j]<point[j+1]){
				temp=point[j];
				point[j]=point[j+1];
				point[j+1]=temp;
				temp = gakuseki[j];
				gakuseki[j] = gakuseki[j+1];
				gakuseki[j+1] = temp; 
			}
		}
	}

	for( i = 0;i<n;i++){
		printf("点数が%d番目に大きい人の学籍番号が%dの人の点数%d\n",i+1,gakuseki[i],a[gakuseki[i]]);
	}
	for(c=0;c<K;c++){
		sum=0;
		count=0;
		printf("グループ%d:",c+1);
		//グループに生徒の点数を追加
		for(j=c,i=0;j<n;j+=K){
			num[j] = gakuseki[j];
			i++;
			sum+=a[gakuseki[j]];
		    
			count+=1;
		}
		//グループ内の学籍番号昇順バブルソート
		for(k=n-1;k>c;k-=K){
			for(j=c;j<n-K;j+=K){
				 if(num[j]>num[j+K]){
					 temp=num[j];
					 num[j]=num[j+K];
					 num[j+K]=temp;
				 }
			}
		}

		//学籍番号，成績平均出力
		for(j=c;j<n;j+=K){
			printf("%d, ",num[j]+1);
		}
		printf("成績平均=%lf\n",(double)sum/count);
	}
	system("pause");
}