#include <stdio.h>
#include <stdlib.h>

int main(void){
    int i,j,a;
    FILE *fp;
    fp= fopen("kuku.txt", "w");
    if (fp == NULL){
        fprintf(stderr , "Cannot open the file \n");
        exit(1);
    }
    for(i = 1;i<10;i++){
        for(j = 1;j<10;j++){
            a = i * j;
            printf("%2d\t",a);
            fprintf(fp , "%2d\t", a);
        }
        printf("\n");
        fprintf(fp , "\n");
    }
    fclose(fp);
}
