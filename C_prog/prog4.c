#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

#define N 1000

double f(double a){
    return a*a+2;
}

int main (void){
    int i,left,right;
    double a,sum,dx;
    
    left = -2;
    right = 2;
    dx = (double)abs(left-right)/N;

    a = left;
    sum = 0.0;
    for(i = 0;i<N;i++){
        sum += (f(a)+f(a+dx))*dx/2;
        a+= dx;
    }
    printf("Answer: %lf\n",sum);
}

