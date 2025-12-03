for f in *_IQTREE.treefile; do
    gene=$(basename "$f" _IQTREE.treefile)
    newick=$(cat "$f" | tr -d '\n')
    echo ">$gene" >> gene_trees.fasta
    echo "$newick" >> gene_trees.fasta
done

