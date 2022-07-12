#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

#define SIZE 10

int main (void){
    int matrix[SIZE][SIZE];
    int a;
    srand ((unsigned) time (NULL));

    // 疑似入力
    for(int i =0;i<SIZE;i++){
        for(int  j =0;j<SIZE;j++){
            a = rand() % 10; //0-9以下の乱数
            matrix[i][j] = a;
        }
    }

    //表示１
    printf("[Before]\n");
    printf("A = \n");
    for(int i =0;i<SIZE;i++){
        for(int  j =0;j<SIZE;j++){
            printf("%d ",matrix[i][j]);
        }
        printf("\n");
    }

    //演算処理
    for(int i =0;i<SIZE;i++){
        for(int  j =0;j<SIZE;j++){
            //対角成分
            if(i==j){
                matrix[i][j] *=-1;
            }
            //上三角
            else if(j>i){
                matrix[i][j] *=3;
            }
            //下三角
            else if(j<i){
                matrix[i][j] *=2;
            }
        }
    }
    //出力(表示2)
    printf("[After]\n");
    printf("A = \n");
    for(int i =0;i<SIZE;i++){
        for(int  j =0;j<SIZE;j++){
            printf("%2d ",matrix[i][j]);
        }
        printf("\n");
    }
}