#include <stdio.h>
#define ROW_SIZE 6
#define COL_SIZE 5

main(void)
{
    int scores[ROW_SIZE][COL_SIZE] = {{80,40,50,100,60},{30,40,50,60,70},{20,10,30,10,10},{41,10,34,11,20},{50,40,10,6,100},{30,10,20,10,50}};
    int i, j;
    int subject_max[COL_SIZE],person_max[COL_SIZE];
    int subject_min[COL_SIZE],person_min[COL_SIZE];
    for(i = 0;i<COL_SIZE;i++){
        subject_max[i] = scores[0][i];
        person_max[i] = 0;
        subject_min[i] = scores[0][i];
        person_min[i] = 0;
        for(j=1;j<ROW_SIZE;j++){
            if(scores[j][i]>subject_max[i]){
                subject_max[i] = scores[j][i];
                person_max[i] = j;
            }
            if(scores[j][i]<subject_min[i]){
                subject_min[i] = scores[j][i];
                person_min[i] = j;
            }
        }
    }
    for(i = 0;i<COL_SIZE;i++){
        printf("Max score of subject(%d) is %d, student No. is %d\n",i,subject_max[i],person_max[i]);
        printf("Min score of subject(%d) is %d, student No. is %d\n",i,subject_min[i],person_min[i]);
    }
}

