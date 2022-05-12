#include <stdlib.h>
#include <stdio.h>

void madd(int a[][10],int b[][10], int c[][10], int m, int n){
  int i, j ,sum;
  for(i = 0; i<m;i++){
    for(j= 0; j<n;j++){
      sum = a[i][j] + b[i][j];
      c[i][j] = sum;
    }
  }
}

int main(){
  int i,j,m,n,a[10][10],b[10][10],c[10][10];
  printf("m n を入力");
  scanf("%d %d",&m,&n);
  printf("1 つの行列を入力\n");
  for(i = 0; i<m;i++){
    for(j= 0; j<n;j++){
      scanf("%d",&a[i][j]);
    }
  }
  printf("2 つ目の行列を入力\n");
  for(i = 0; i<m;i++){
    for(j= 0; j<n;j++){
      scanf("%d",&b[i][j]);
    }
  }
  madd(a,b,c,m,n);
  printf("答えは\n");
  for(i = 0; i<m;i++){
    for(j= 0; j<n;j++){
      printf("%d ", c[i][j]);
    }
    printf("\n");
  }
  system("pause");


}