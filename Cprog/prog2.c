#include <stdio.h>
#include <math.h>



void Area_rectangle(double a,double b,int c,double *d){
    double rad_c = (double)c *M_PI / 180;
    *d = a*b*sin(rad_c)/2;
}

int main(){
    int c;
    double a,b,d;
    //入力
    printf("三角形の底辺：");
    scanf("%lf",&a);
    printf("斜辺：");
    scanf("%lf",&b);
    printf("角度(°):");
    scanf("%d",&c);



    Area_rectangle(a,b,c,&d);
    printf("d=%f\n",d);
    return 0;
}