#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

#define COL_SIZE 5

struct scores{
    int id;
    int score[5];
};

int main (void){
    struct scores data[6] = {
       {101,{80,40,50, 100,60}},
       {204, {30, 40, 50, 60, 70}},
       {308, {20, 10, 30, 10, 10}},
       { 209, {41, 10, 34, 11, 20}}, 
       {301, {50, 40, 10, 6, 100}}, 
       {500, {30, 10, 20, 10, 50}},
    };


    int i, j;
    int subject_max[COL_SIZE],person_max[COL_SIZE];
    int subject_min[COL_SIZE],person_min[COL_SIZE];
    for(i = 0;i<COL_SIZE;i++){
        subject_max[i] = data[0].score[i];
        person_max[i] =data[0].id;
        subject_min[i] = data[0].score[i];
        person_min[i] = data[0].id;
        for(j=1;j<6;j++){
            if(data[j].score[i]>subject_max[i]){
                subject_max[i] = data[j].score[i];
                person_max[i] = data[j].id;
            }
            if(data[j].score[i]<subject_min[i]){
                subject_min[i] = data[j].score[i];
                person_min[i] = data[j].id;
            }
        }
    }
    for(i = 0;i<COL_SIZE;i++){
        printf("Max score of subject(%d) is %d, student No. is %d\n",i,subject_max[i],person_max[i]);
        printf("Min score of subject(%d) is %d, student No. is %d\n",i,subject_min[i],person_min[i]);
    }
}

