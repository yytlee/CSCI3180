ta_ranking: ta_ranking.cob
	cobc -x ta_ranking.cob

c: ta_ranking.c
	gcc ta_ranking.c -o ta_ranking_c

cindy: ./source/cindy.cob
	cobc -x ./source/cindy.cob

soa: ./source/soa.cob
	cobc -x ./source/soa.cob

rm:
	rm ta_ranking ta_ranking_c soa cindy
