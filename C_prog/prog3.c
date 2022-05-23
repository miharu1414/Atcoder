#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

#define SIZE 11

int main (void){
    int count[SIZE];
    int a,i,j;
    srand ((unsigned) time (NULL));

    for(i = 0;i<11;i++) count[i] = 0;
    // 疑似入力

    for(i = 0;i<2000;i++){
        a = rand() % 10; //0-9以下の乱数
        a +=1;//1-10の整数値
        count[a]+=1;
    }

    for(i = 1;i<=10;i++){
        if(count[i]==0){
            continue;
        }
        printf("%2d: %3d time(s):",i,count[i]);
        for(j = 0;j<count[i]/10;j++){
            printf("*");
        }
        printf("\n");
    }
}