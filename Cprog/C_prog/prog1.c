#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

#define SIZE 101

int main (void){
    double a[SIZE];
    int i;
    double sum;

    for(int i = 1; i<=100;i++){
        if(i%3==0){
            a[i] = i*i;
        }
        else if(i%3==1){
            a[i] =-i;
        }
        else{
            a[i] = (double)1/(i*i);

        }
    }

    sum = 0;
    for(int i = 1; i<=100;i++){
        sum += a[i];
    }
    printf("Answer:%lf\n",sum);
}