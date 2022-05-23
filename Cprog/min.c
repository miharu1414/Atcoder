#include <stdio.h>
#define SIZE 10

main(void)
{
    int scores[SIZE];
    int i;
    int min;
    for ( i =0; i < SIZE; i ++) {
        printf ("input score[%d]:", i);
        scanf("%d", &scores[i]);
    }
    for (i = 0; i < SIZE; i ++){
        if (i==0){
            min = scores[i];
        }
        else if(min>scores[i]){
            min = scores[i];
        }
        
    }
    printf("Min = %d \n", min);
    return 0;
}