parallel -j 20 'base={.}; java -jar ~/software/macse_v2.04.jar -prog exportAlignment \
-align "${base}.fa" \
-codonForInternalStop NNN \
-codonForInternalFS --- \
-charForRemainingFS - \
-codonForFinalStop --- \
-out_NT "${base}_noFS_NT.fasta" \
-out_AA "${base}_noFS_AA.fasta"' ::: *.fa
