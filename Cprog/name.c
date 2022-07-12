#include <stdio.h>
#include <string.h>
int main(void)
{
    char firstname[64], lastname[64],name[64],Lastname[64];
    int len, n;

    //入力
    printf("Input your first name: ");
    scanf("%s", firstname);
    printf("Input your Last name: ");
    scanf("%s", lastname);

    //空白挿入
    len = strlen(firstname);
    firstname[len] = ' ';
    //結合
    strcpy(name,strcat(firstname,lastname)); /* 文字列のstr1+str2 */
 
    //出力
    printf("Your name is %s.\n", name); /*“hello, world”*/
    return 0;
}
