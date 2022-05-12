//一様分布で点数を生成


#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include<math.h>

int main(){
	int data[10000],data_point[1000],number_gakuseki[1000],group_member[250][250],group_rank[1000];
	int k,roop,left_man,n,i,pos_gr,now,j,m,temp_p,temp_num,point;
	double mean_group[1000];
    srand(time(NULL)*12345);
	printf("生徒の人数を入力してください：");
	scanf("%d", &n);
	printf("グループ数を入力してください：");
	scanf("%d", &k);
	for(i = 0; i<n;){
		printf("学籍番号 %d の生徒の点数:",i+1);
		point = 101*rand()/(RAND_MAX+1);
        data[i] = point;
        printf("%d\n", point);
		data_point[i] = data[i];
		number_gakuseki[i] = i;//点数のデータと添え字をそろえる．
		i++;
	}
	//挿入法ソート  (降順)
	for(m = 0;m<n-1;m++){
		for( temp_p = data[m+1], temp_num = number_gakuseki[m+1],i = m;i>=0;i--){
			if(temp_p < data[i])break; //降順，大きい順だから
			data[i+1] = data[i];
			number_gakuseki[i+1] = number_gakuseki[i];
		}
		data[i+1] = temp_p;
		number_gakuseki[i+1] = temp_num;
	}
	printf("\n挿入法ソート完了\n\n");
	printf("点数(降順):");
	for(i=0;i<n;i++) {
		if(i%20==0) printf("\n");
		printf("%d ",data[i]);
	}
	printf("\n対応する学籍番号:");
	for(i=0;i<n;i++){
		if(i%20==0) printf("\n");
		printf("%d ",number_gakuseki[i]+1);
	}
	printf("\n\n");

	/*仕様のメモ
		mean_group[i] : iグループの平均値
		group_member[i][0]：iグループの人数
		group_member[i][j]：iグループのj番目の人の学籍番号 j>=1
		group_rank[i]：i番目に小さいグループの番号を返す
		　　→group_rank[pos_gr]でpos_gr番目に小さいグループの番号を返す
		now ：何人目の人を振っているか
		roop：何巡目か
		number_gakuseki[i]：i番目に大きい人の学籍番号
		data_point[i]:学籍番号がiの人の得点
	*/

	//ここからgroup分けに関する処理

	for(i = 0;i<k;i++){
		mean_group[i] = 0;
		group_rank[i] = i;//最初はグループ1から随時入れていくので
	}
	for(i = 0;i<k;i++)  group_member[i][0] = 0;//i+1番目のグループの人数を[i][0]に格納する (出力の時に使用)

	left_man = n;
	pos_gr = 0; //何番目のグループか（平均値が小さい方から）
	now = 0;//何人目か
	roop = 1; //何巡目か
	for(roop = 1; roop <= (n + k - 1)/k; roop++){//何巡必要か計算　切り上げ
		for(i = 0; i < k&& left_man>0; i++){
			group_member[group_rank[i]][roop] = number_gakuseki[now];
			left_man--;
			now++;
			group_member[group_rank[i]][0]++;
		}
		if(left_man>0){
			for(i=0;i<k;i++){//各グループの平均値を計算
				mean_group[i] = 0;
				for(j = 1;j<=group_member[i][0];j++){
					mean_group[i] += data_point[group_member[i][j]];
				}
				mean_group[i] /= roop; //(roopとgroup_member[i][0]はここでは同じ)
			}
			//挿入法ソート  (昇順)
			//平均値が小さいグループ順にgroup_rank[]を並べ替える．
			//初期値にgroup_rank[i] = iを入れていることで，平均値を比較し，ソートする過程でグループ番号も入れ替わる仕組み →　平均値が小さい順にグループ番号がa[0],a[1],...に保存される．
			//つまり，group_rank[i]でi番目に小さいグループを返してくれる

			//ソートを行う前にgroup_rankは初期化する必要がある．
			for(i = 0;i<k;i++) group_rank[i] = i; //平均値はグループ1,2,...と列挙するため，それに順位を対応させるため
			for(m = 0;m<k-1;m++){
				for( temp_p = mean_group[m+1], temp_num = group_rank[m+1],i = m;i>=0;i--){
					if(temp_p >= mean_group[i])break; //小さい順，昇順
					mean_group[i+1] = mean_group[i];
					group_rank[i+1] = group_rank[i];
				}
				mean_group[i+1] = temp_p;
				group_rank[i+1] = temp_num;
			}
		}
	}
	for(i=0;i<k;i++){//各グループの平均値を計算
		mean_group[i] = 0;
		for(j = 1;j<=group_member[i][0];j++){
			mean_group[i] += data_point[group_member[i][j]];
		}
		mean_group[i] /= group_member[i][0]; //group_member[i][0]を使う ここではroopだめ，グループごとに人数が違う可能性がある
	}

	//グループiごとに学籍番号順にソート
	for(i = 0; i < k;i++){
		for(m = 1;m < group_member[i][0] ;m++){
				for( temp_p = group_member[i][m+1],j = m;j>=1;j--){
					if(temp_p >= group_member[i][j]) break; //小さい順，昇順
					group_member[i][j+1] = group_member[i][j];
				}
				group_member[i][j+1] = temp_p;
			}
	}


	for(i = 0;i<k;i++){
		printf("グループ%d：",i+1);
		for(j = 1;j<=group_member[i][0];j++){
			printf(" %d",group_member[i][j]+1);
			if(j!=group_member[i][0]) printf(",");
			if(j%20==0) printf("\n　　　　　");
		}
		printf(" (成績平均 ＝ %0.2lf)\n",mean_group[i]);
		printf("合計点 ＝ %d\n",(int)(mean_group[i]*group_member[i][0]));
	}
	printf("\n\n");

	system("pause");
}