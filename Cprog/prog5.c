#include <stdio.h>
#include <stdlib.h>
#include <math.h>



int max(int x,int y){
    if(x>=y) return x;
    else return y;
}

int min(int x,int y){
    if(x<=y) return x;
    else return y;
}

struct score{
    int science;
    int math;
    int english;
};

int main(){
    FILE *fin;
    char str[256],filename[] = "score.txt";;
    int x,i,j,maxdata,mindata;
    double ave;

    fin = fopen(filename,"r");
    if (fin == NULL) {
        printf("Cannot open the file \n");
        exit(1);
    }

    //入力受け取り
    i = 0;
    struct score data[5];
    while(fscanf(fin,"%d,%d,%d",&data[i].science,&data[i].math,&data[i].english)!=EOF){

        i+=1;
    }

    //理科科目の処理
    for(j = 0;j<i;j++){
        if(j==0){
            mindata = data[j].science;
            maxdata = data[j].science;
            ave = data[j].science;
        }
        else{
            mindata = min(mindata,data[j].science);
            maxdata = max(maxdata,data[j].science);
            ave += data[j].science;
        }
    }
    ave /= i;
    printf("science max score = %d min score = %d average socre = %f\n",maxdata,mindata,ave);


    //数学科目の処理
    for(j = 0;j<i;j++){
        if(j==0){
            mindata = data[j].math;
            maxdata = data[j].math;
            ave = data[j].math;
        }
        else{
            mindata = min(mindata,data[j].math);
            maxdata = max(maxdata,data[j].math);
            ave += data[j].math;
        }
    }
    ave /= i;
    printf("math max score = %d min score = %d average socre = %f\n",maxdata,mindata,ave);

    //英語科目の処理
    for(j = 0;j<i;j++){
        if(j==0){
            mindata = data[j].english;
            maxdata = data[j].english;
            ave = data[j].english;
        }
        else{
            mindata = min(mindata,data[j].english);
            maxdata = max(maxdata,data[j].english);
            ave += data[j].english;
        }
    }
    ave /= i;
    printf("english max score = %d min score = %d average socre = %f\n",maxdata,mindata,ave);
    return 0;
}   