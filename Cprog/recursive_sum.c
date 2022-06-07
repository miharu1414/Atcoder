#include <stdio.h>

int sum(int n){
    if(n==0) return 0;
    return n + sum(n-1);
}

int main(void){
    int n,ans;
    printf("Input:");
    scanf("%d",&n);
    ans = sum(n);
    printf("%d\n",ans);
}