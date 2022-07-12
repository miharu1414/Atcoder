#include <stdio.h>
#include <string.h>


char change(char x){
    if (x>=97) return 'A'+x-'a';   //小文字⇒大文字
    else if(x>=65) return 'a' + x - 'A';  //大文字⇒小文字
    else return x; //数字など無変更
}

int main(void){
    //宣言
    char input[101],output[101];
    int len, i;

    //入力
    printf("Input string: ");
    scanf("%s", input);

    //変換
    len = strlen(input);
    for(i = 0;i<len;i++){
        output[i] = change(input[i]);
    }
    output[len] = input[len];

    // 出力
    printf("Output string: %s\n", output); /*“hello, world”*/
    return 0;
}