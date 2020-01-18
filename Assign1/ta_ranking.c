#include <stdio.h>
#include <string.h>
#include <stdlib.h>

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

char* substr(char *src, int start, int end)
{
	int len = end - start + 1;
	char *str = (char*)malloc(sizeof(char) * len);
	for(int i = start; (i < end) && (*src != '\0'); i++)
	{
		*str = *(src + i);
		str++;
	}
	*str = '\0';
	return str - len + 1;
}

int main(void){
    int num_instr = 0;
    int num_candi = 0;
    INSTRUCTOR *instr = (INSTRUCTOR*)malloc(sizeof(INSTRUCTOR*));
    CANDIDATE *candi = (CANDIDATE*)malloc(sizeof(CANDIDATE*));
    char tmp[147];

    FILE *instr_fp = fopen("./testcase/instructors.txt", "r");
    if(instr_fp == NULL)printf("error");

    while(fgets(tmp, 125, instr_fp) != NULL){
        //printf("%s\n", tmp);
        num_instr++;
        instr = (INSTRUCTOR*)realloc(instr, sizeof(INSTRUCTOR) * num_instr);
        sscanf(tmp, "%d", &instr[num_instr - 1].courseID);
        int pt = 5;
        for(int i = 0; i < 3; i++){
            instr[num_instr - 1].req_skill[i] = substr(tmp, pt, pt + 15);
            pt += 15;
            //printf("-> %s\n", instr[num_instr - 1].req_skill[i]);
        }
        for(int i = 0; i < 5; i++){
            instr[num_instr - 1].opt_skill[i] = substr(tmp, pt, pt + 15);
            pt += 15;
            //printf("-> %s\n", instr[num_instr - 1].opt_skill[i]);
        }

        fgets(tmp, 125, instr_fp);
    }
    fclose(instr_fp);

    FILE *candi_fp = fopen("./testcase/candidates.txt", "r");
    if(candi_fp == NULL)printf("error");

    while(fgets(tmp, 146, candi_fp) != NULL){
        //printf("%s\n", tmp);
        num_candi++;
        candi = (CANDIDATE*)realloc(candi, sizeof(CANDIDATE) * num_candi);
        sscanf(tmp, "%d", &candi[num_candi - 1].ID);
        int pt = 11;
        for(int i = 0; i < 8; i++){
            candi[num_candi - 1].skill[i] = substr(tmp, pt, pt + 15);
            pt += 15;
            //printf("-> %s\n", candi[num_candi - 1].skill[i]);
        }
        sscanf(substr(tmp, pt, pt + 15), "%d %d %d", &candi[num_candi - 1].pref[0], &candi[num_candi - 1].pref[1], &candi[num_candi - 1].pref[2]);
        //printf("%d %d %d\n", candi[num_candi - 1].pref[0], candi[num_candi - 1].pref[1], candi[num_candi - 1].pref[2]);
        fgets(tmp, 146, instr_fp);
    }
    fclose(candi_fp);

    return 0;
}