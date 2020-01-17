#include <stdio.h>
#include <string.h>

typedef struct instructor{
    int courseID;
    char *req_skill[3];
    char *opt_skill[5];
}INSTRUCTOR;

typedef struct candidate{
    int ID;
    char *skill[8];
    int pref[4];
}CANDIDATE;

int main(void){

    FILE *instr_fp = fopen("/testcase/instructors.txt", "r");
    if(instr_fp == NULL)printf("error");

    s

    FILE *candi_fp = fopen("/testcase/candidates.txt", "r");
    if(candi_fp == NULL)printf("error");

    fclose(instr_fp);
    return 0;
}