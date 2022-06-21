#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>


int main (void){
    int i;
    double x,dx,max,max_x;
    srand ((unsigned) time (NULL));

    x =10*rand()/(RAND_MAX+1.0) ; //0-10以下の乱数

    dx = 0.00001;
    max_x = x;
    max = sin(x);
    while(abs(sin(x))>0.000001){
        x += dx;
        // printf("%lf \n",sin(x));
        if(max<sin(x)){
            max = sin(x);
            max_x = x;
        }
    }
    printf("max = %lf, x = %lf\n",max,max_x);
    return 0;
}


