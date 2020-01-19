000000*
000000* CSCI3180 Principles of Programming Languages
000000*
000000* --- Declaration ---
000000*
000000* I declare that the assignment here submitted is original except for source
000000* material explicitly acknowledged. I also acknowledge that I am aware of
000000* University policy and regulations on honesty in academic work, and of the
000000* disciplinary guidelines and procedures applicable to breaches of such policy
000000* and regulations, as contained in the website
000000* http://www.cuhk.edu.hk/policy/academichonesty/
000000*
000000* Assignment 1
000000* Name : Lee Tsz Yan
000000* Student ID : 1155110177
000000* Email Addr : 1155110177@link.cuhk.edu.hk
000000*                                                               
000000 *****************************************************************
000000  IDENTIFICATION DIVISION.
000000  PROGRAM-ID.  TA_RANKING.
000000  AUTHOR. LEE TSZ YAN. 
000000  INSTALLATION. COBOL DEVELOPMENT CENTER. 
000000  DATE-WRITTEN. 19/01/2020. 
000000  DATE-COMPILED. 01/01/08. 
000000  SECURITY. NON-CONFIDENTIAL.
000000 *****************************************************************
       ENVIRONMENT DIVISION.
       INPUT-OUTPUT SECTION.
       FILE-CONTROL.
           SELECT INSTRUCTORS ASSIGN TO 'testcase/instructors.txt'
           SELECT CANDIDATES ASSIGN TO 'testcase/candidates.txt'
           SELECT OUTPUT_FILE ASSIGN TO 'testcase/output.txt'
           ORGANIZATION IS LINE SEQUENTIAL.
       DATA DIVISION.
       FILE SECTION.
       FD INSTRUCTORS.
