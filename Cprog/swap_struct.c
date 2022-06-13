#include <stdio.h>



struct  three_num{
    int a;
    int b;
    int c;
    /* data */
};

void swap(struct three_num *v1,struct three_num *v2){
    int temp;
    temp = v1->a;
    v1->a = v2->a;
    v2->a = temp;

    temp = v1->b;
    v1->b = v2->b;
    v2->b = temp;

    temp = v1->c;
    v1->c = v2->c;
    v2->c = temp;
}


int main(){
    int i,sum1,sum2 ;
    struct three_num v1;
    struct three_num v2;
    printf("空白区切り三つの要素を入力してください．\n");
    printf("v1:");
    scanf("%d %d %d",&v1.a,&v1.b,&v1.c);
    
    printf("v2:");
    scanf("%d %d %d",&v2.a,&v2.b,&v2.c);
    sum1 = v1.a + v1.b + v1.c;
    sum2 = v2.a + v2.b + v2.c;
    if(sum1>sum2){
        printf("v1の和:%d > v2の和:%dなので入れ替える.\n",sum1,sum2);
        swap(&v1,&v2);
    }
    else{
         printf("v1の和:%d > v2の和:%dでないので入れ替えない.",sum1,sum2);
    }
    printf("確認\n");
    printf("v1の各メンバ %d %d %d\n",v1.a,v1.b,v1.c);
    printf("v2の各メンバ %d %d %d\n",v2.a,v2.b,v2.c);
}