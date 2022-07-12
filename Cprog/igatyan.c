#include<stdio.h>
#include<stdlib.h>
#include<time.h>

struct score{
int science;
int math;
int english;
};


int main(void){
int i;
struct score a[5];
FILE *fp;
fp = fopen("score.txt", "r");
if (fp == NULL) {
fprintf(stderr, "Cannot open the file¥n");
exit(1);
}
i = 0;
while (fscanf(fp, "%d, %d, %d", &a[i].science, &a[i].math, &a[i].english) != EOF){
i+=1;
}
fclose(fp);
int score_s[2] = {0, 100};
int score_m[2] = {0, 100}; 
int score_e[2] = {0, 100};
double ave_s = 0;
double ave_m = 0;
double ave_e = 0;
for (i = 0; i < 5; i++){
if (a[i].science > score_s[0]) score_s[0] = a[i].science;
if (a[i].science < score_s[1]) score_s[1] = a[i].science;
if (a[i].math > score_m[0]) score_m[0] = a[i].math;
if (a[i].math < score_m[1]) score_m[1] = a[i].math;
if (a[i].english > score_e[0]) score_e[0] = a[i].english;
if (a[i].english < score_e[1]) score_e[1] = a[i].english;
ave_s += a[i].science;
ave_m += a[i].math;
ave_e += a[i].english;
}

printf("science max score = %d min score = %d average score = %f¥n", score_s[0], score_s[1], ave_s/5);
printf("math max score = %d min score = %d average score = %f¥n", score_m[0], score_m[1], ave_m/5);
printf("english max score = %d min score = %d average score = %f¥n", score_e[0], score_e[1], ave_e/5);
return 0;
}