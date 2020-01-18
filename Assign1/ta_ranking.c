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
    int pref[3];
}CANDIDATE;

char* substr(char *src, int start, int end){
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

int req_satisf(INSTRUCTOR in, CANDIDATE ca){
    for(int i = 0; i < 3; i++){
        for(int j = 0; j < 8; j++){
            if(strcmp(in.req_skill[i], ca.skill[j]) == 0) break;
            if(j == 7) return 0;
        }
    }
    return 1;
}

double score(INSTRUCTOR in, CANDIDATE ca){
    if(req_satisf(in, ca) == 0) return 0;
    double s = 1;
    for(int i = 0; i < 5; i++){
        for(int j = 0; j < 8; j++){
            if(strcmp(in.opt_skill[i], ca.skill[j]) == 0){
                s++;
                break;
            }
        }
    }

    if(ca.pref[0] == in.courseID) s+=1.5;
    else if(ca.pref[1] == in.courseID) s++;
    else if(ca.pref[2] == in.courseID) s+=0.5;
    return s;
}

void print_score(INSTRUCTOR *instr, CANDIDATE *candi, int in, int ca){
    for(int i = 0; i < in; i++){
        printf("%d: ", instr[i].courseID);
        for(int j = 0; j < ca; j++){
            printf("%.1f ", score(instr[i], candi[j]));
        }
        printf("\n");
    }
}

int main(void){
    int num_instr = 0;
    int num_candi = 0;
    INSTRUCTOR *instr = (INSTRUCTOR*)malloc(sizeof(INSTRUCTOR));
    CANDIDATE *candi = (CANDIDATE*)malloc(sizeof(CANDIDATE));
    char tmp[147];

    FILE *instr_fp = fopen("./testcase/instructors.txt", "r");
    if(instr_fp == NULL) printf("error");

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
    if(candi_fp == NULL) printf("error");

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

    FILE *output_fp = fopen("output.txt", "w");
    if(output_fp == NULL) printf("error");

    for(int i = 0; i < num_instr; i++){
        int suit_candi = 0;
        int rank[3][2] = {{0}};
        for(int j = 0; j < num_candi; j++){
            int s = score(instr[i], candi[j]);
            if(s > rank[0][1]){
                suit_candi++;
                rank[2][0] = rank[1][0];
                rank[2][1] = rank[1][1];
                rank[1][0] = rank[0][0];
                rank[1][1] = rank[0][1];
                rank[0][0] = candi[j].ID;
                rank[0][1] = s;
            }
            else if(s > rank[1][1]){
                suit_candi++;
                rank[2][0] = rank[2][0];
                rank[2][1] = rank[2][1];
                rank[1][0] = candi[j].ID;
                rank[1][1] = s;
            }
            else if(s > rank[2][1]){
                suit_candi++;
                rank[2][0] = candi[j].ID;
                rank[2][1] = s;
            }
        }
        fprintf(output_fp, "%d ", instr[i].courseID);
        for(int k = 0; k < 3; k++){
            if(rank[k][0] == 0 && rank[k][1] == 0){
                fputs("0000000000 ", output_fp);
            }
            else fprintf(output_fp, "%d ", rank[k][0]);
        }
        fputs("\n", output_fp);
    }

    //print_score(instr, candi, num_instr, num_candi);
    return 0;
}