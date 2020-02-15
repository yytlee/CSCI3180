/*
 * CSCI3180 Principles of Programming Languages
 *
 * --- Declaration ---
 *
 * I declare that the assignment here submitted is original except for source
 * material explicitly acknowledged. I also acknowledge that I am aware of
 * University policy and regulations on honesty in academic work, and of the
 * disciplinary guidelines and procedures applicable to breaches of such policy
 * and regulations, as contained in the website
 * http://www.cuhk.edu.hk/policy/academichonesty/
 *
 * Assignment 1
 * Name : Lee Tsz Yan
 * Student ID : 1155110177
 * Email Addr : tylee8@cse.cuhk.edu.hk
 */

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
    int i;
	for(i = start; (i < end) && (*src != '\0'); i++)
	{
		*str = *(src + i);
		str++;
	}
	*str = '\0';
	return str - len + 1;
}

int req_satisf(INSTRUCTOR in, CANDIDATE ca){
    int i, j;
    for(i = 0; i < 3; i++){
        for(j = 0; j < 8; j++){
            if(strcmp(in.req_skill[i], ca.skill[j]) == 0) break;
            if(j == 7) return 0;
        }
    }
    return 1;
}

double score(INSTRUCTOR in, CANDIDATE ca){
    if(req_satisf(in, ca) == 0) return 0;
    double s = 1;
    int i, j;
    for(i = 0; i < 5; i++){
        for(j = 0; j < 8; j++){
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

void print_score(INSTRUCTOR *instr, CANDIDATE *candi, int in, int ca, int mode){
    int i, j;
    for(i = 0; i < in; i++){
        printf("%d: ", instr[i].courseID);
        for(j = 0; j < ca; j++){
            if(!mode)printf("%.1f ", score(instr[i], candi[j]));
            else {
                if(score(instr[i], candi[j]) > 0){
                    printf("%d %.1f ", (candi[j].ID)%1155000000, score(instr[i], candi[j]));
                }
            }
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
    int i, j, k;

    FILE *instr_fp = fopen("./instructors.txt", "r");
    if(instr_fp == NULL){
        printf("non-existing file!\n");
        exit(-1);
    }

    while(fgets(tmp, 126, instr_fp) != NULL){
        //printf("%s\n", tmp);
        num_instr++;
        instr = (INSTRUCTOR*)realloc(instr, sizeof(INSTRUCTOR) * num_instr);
        sscanf(tmp, "%d", &instr[num_instr - 1].courseID);
        int pt = 5;
        for(i = 0; i < 3; i++){
            instr[num_instr - 1].req_skill[i] = substr(tmp, pt, pt + 15);
            pt += 15;
            //printf("-> %s\n", instr[num_instr - 1].req_skill[i]);
        }
        for(i = 0; i < 5; i++){
            instr[num_instr - 1].opt_skill[i] = substr(tmp, pt, pt + 15);
            pt += 15;
            //printf("-> %s\n", instr[num_instr - 1].opt_skill[i]);
        }

        fgets(tmp, 126, instr_fp);
    }
    fclose(instr_fp);

    FILE *candi_fp = fopen("./candidates.txt", "r");
    if(candi_fp == NULL){
        printf("non-existing file!\n");
        exit(-1);
    }

    while(fgets(tmp, 146, candi_fp) != NULL){
        //printf("%s\n", tmp);
        num_candi++;
        candi = (CANDIDATE*)realloc(candi, sizeof(CANDIDATE) * num_candi);
        sscanf(tmp, "%d", &candi[num_candi - 1].ID);
        int pt = 11;
        for(i = 0; i < 8; i++){
            candi[num_candi - 1].skill[i] = substr(tmp, pt, pt + 15);
            pt += 15;
            //printf("-> %s\n", candi[num_candi - 1].skill[i]);
        }
        sscanf(substr(tmp, pt, pt + 15), "%d %d %d", &candi[num_candi - 1].pref[0], &candi[num_candi - 1].pref[1], &candi[num_candi - 1].pref[2]);
        //printf("%d %d %d\n", candi[num_candi - 1].pref[0], candi[num_candi - 1].pref[1], candi[num_candi - 1].pref[2]);
        fgets(tmp, 146, instr_fp);
    }
    fclose(candi_fp);

    FILE *output_fp = fopen("output.txt", "w");                                      // remember to change file name
    if(output_fp == NULL){
        printf("non-existing file!\n");
        exit(-1);
    }

    for(i = 0; i < num_instr; i++){
        double rank[3][2] = {{0}};
        for(j = 0; j < num_candi; j++){
            double s = score(instr[i], candi[j]);
            if(s > rank[0][1] || (s == rank[0][1] && candi[j].ID < rank[0][0])){
                rank[2][0] = rank[1][0];
                rank[2][1] = rank[1][1];
                rank[1][0] = rank[0][0];
                rank[1][1] = rank[0][1];
                rank[0][0] = candi[j].ID;
                rank[0][1] = s;
            }
            else if(s > rank[1][1] || (s == rank[1][1] && candi[j].ID < rank[1][0])){
                rank[2][0] = rank[1][0];
                rank[2][1] = rank[1][1];
                rank[1][0] = candi[j].ID;
                rank[1][1] = s;
            }
            else if(s > rank[2][1] || (s == rank[2][1] && candi[j].ID < rank[2][0])){
                rank[2][0] = candi[j].ID;
                rank[2][1] = s;
            }
        }
        fprintf(output_fp, "%d ", instr[i].courseID);
        for(k = 0; k < 3; k++){
            if(rank[k][0] == 0 && rank[k][1] == 0){
                fputs("0000000000 ", output_fp);
            }
            else fprintf(output_fp, "%.0f ", rank[k][0]);
        }
        fputs("\n", output_fp);
    }
    fclose(output_fp);

    free(instr);
    free(candi);

    //print_score(instr, candi, num_instr, num_candi, 1);
    return 0;
}