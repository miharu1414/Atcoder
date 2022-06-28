#include <stdio.h>
#include <stdlib.h>



void Upper(char *s){
	int	i;
	i = 0;
	while( s[i] != '\0' ){
        if (s[i]>=97) s[i]= 'A'+s[i]-'a';   //小文字⇒大文字
		i++;
    }
}
int main(int argc , char *argv[]){
    FILE *fin;
    char str[256];
    fin = fopen(argv[1],"r");
    if (fin == NULL) {
        printf("Cannot open the file \n");
        exit(1);
    }
    while (fgets(str , 256, fin) != NULL){
        Upper(str);
        printf ("%s", str);
    }
    fclose(fin);
    return 0;
}