#include <stdio.h>
#include <math.h>

double f(double x){
    return pow(x,4) -5* pow(x,3) +5*pow(x,2)+5*x-6;
}
double df(double x){
    return 4*pow(x,3)-15*pow(x,2)+10*x+5;
}

int main(){
    double x0,x1,e = 0.0000001;
    printf("初期値:");
    scanf("%lf",&x1);
    do{
        x0 = x1;
        x1 = x0 - f(x0)/df(x0);
    }while(abs(x0-x1)>=e);

    printf("x = %f\n",x1);


    return 0;
}