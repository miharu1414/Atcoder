#include <stdio.h>

int check_prime_number(int a){
    int i;
    for(i=2;i*i<=a;i++){
        if(a%i==0){
            return 0;
        }
    }
    return 1;
}

int main(void){
    int i;
    int max_n = 30;
    for(i = 2;i<=max_n;i++){
        if(check_prime_number(i)){
            printf("%d\n" ,i);
        }
    }
}