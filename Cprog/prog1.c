#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define STR_SIZE 201
#define SIZE 26

void count_alphabet(char s,int count[SIZE]){
        if(s>=65 && s<97) s = 'a' + s - 'A'; //大文字⇒小文字
        count[int(s-'a')] += 1;

}
int main(){
    char str[STR_SIZE];
    int count[SIZE];
    int i;
    //初期化
    for (i = 0;i<SIZE;i++) count[i] = 0;

    printf("Input characters:");
    scanf("%s",str);




     //カウント
    for (i = 0;i<(int)strlen(str);i++){
        count_alphabet(str[i],count);
    }
    //出力
    for(i = 0;i<SIZE;i++){
        if(count[i] > 0){
            printf("%c/%c: %d\n",(char)(i+'a'),(char)(i+'A'),count[i]);
        }
    }

    return 0;

}