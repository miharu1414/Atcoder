#include <stdio.h>

void print_kuku_Ndan(int dan){
    int i;
    for(i=1;i<=9;i++){
        printf("%2d  ",dan*i);
    }
}
int main(void){
    int i;
    for(i=1;i<=9;i++){
        print_kuku_Ndan(i);
        printf("\n");
    }

}