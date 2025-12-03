#ls *.fa | parallel -j 25 'iqtree2 -s {} -st CODON -m MG+F3X4+R3 -te ELLSMG2.treefile -T AUTO --prefix {.}_IQTREE > {.}.log 2>&1'

ls *.fa | parallel -j 30 --joblog parallel.log --halt soon,fail=0 '
  iqtree2 -s {} \
          -st CODON \
          -m MG+F3X4+R3 \
          -te {.}.nwk \
          -T AUTO \
          --prefix {.}_IQTREE \
  > {.}.log 2>&1 || echo "FAILED: {}" >> failed_jobs.txt
'

