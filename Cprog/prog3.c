#include <stdio.h>
#include <math.h>
#include <string.h>

struct  student_data{
    char name[20];
    int age;
};


int check(char name1[20],char name2[20]){
    int i,ok = 1;
    if ((int)strlen(name1)!=(int)strlen(name2)){
        return 0;
    }
    for(i = 0;i<(int)strlen(name1);i++){
        if(name1[i]!=name2[i]){
            ok = 0;
            return 0;
        }
    }
    return 1;
    
}

int main(){
    char name[20];
    int i;
    //入力

    struct student_data data[5] ={
        {"Suzuki",16},
        {"Tanaka",20},
        {"Sato",25},
        {"Yamada",30},
        {"Aoki",35},
    };
    
    while(1){
        printf("Input name:");
        scanf("%s",name);
        if(name[0]=='-') break;

        for(i = 0;i<5;i++){
            if(check(data[i].name,name)){
                printf("Age: %d\n",data[i].age);
            }
        }
    }
    return 0;
}