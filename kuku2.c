#include <stdio.h>
#include <stdlib.h>
int main(void){
    FILE *fp;
    fp = fopen("kuku.txt", "w");
    if (fp == NULL) {
        fprintf(stderr, "Cannot open the file¥n");
        exit(1);
    }
    int kazu;
    for (int i = 1; i < 10; i++){
        for (int j = 1; j < 10; j++){
            kazu = i*j;
            fprintf(fp, "%2d\t", kazu);
            printf("%2d\t", kazu);
        }
        fprintf(fp, "\n");
        printf("\n");
    }    
    fclose(fp);

    return 0;
}