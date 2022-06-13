#include <stdio.h>

void swap(int *a,int *b){
    int temp;
    temp = *a;
    *a = *b;
    *b = temp;
}

void order(int *x,int *y, int *z){
    if (*x < *y) swap(x,y);
    if (*x < *z) swap(x,z);
    if(*y<*z) swap(y,z);
}

int main(){
    int a, b, c;
    printf("空白区切りで3つの数字a,b,cを入力してください:");
    scanf("%d %d %d",&a,&b,&c);
    order(&a,&b,&c);
    printf("%d %d %d\n",a,b,c);
}