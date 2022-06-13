#include <stdio.h>
#define SIZE 10

void reverseArray(int *a, int *b){
    int i;
    for(i = 0;i<SIZE;i++){
        b[i] = a[SIZE-i-1];
    }

}
int main(){
    int a[SIZE],a_rev[SIZE];
    int i;

    printf("10この数字を改行区切りで入力してください:\n");
    for(i = 0;i<SIZE;i++){
        scanf("%d",&a[i]);
    }
    reverseArray(a,a_rev);
    printf("Input vector is:         ");
    for(i = 0;i<SIZE;i++){
        printf("%d,",a[i]);
    } 
    printf("\nInversed vector is:      ");
    for(i = 0;i<SIZE;i++){
        printf("%d,",a_rev[i]);
    } 
    printf("\n");
    return 0;

}