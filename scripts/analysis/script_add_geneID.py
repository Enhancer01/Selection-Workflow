import pandas as pd

# Load the gene ID mapping (no header, tab-separated)
gene_map = pd.read_csv("V12_geneID", sep="\t", header=None, names=["Orthomam_ID", "Gene_Symbol"])

# Load the RELAX output with FDR
relax_df = pd.read_csv("Bmal-allgenes_relax_Pval-Kval_with_FDR.tsv", sep="\t")

# Ensure consistent data types for merge (in case one is str and the other is int)
gene_map["Orthomam_ID"] = gene_map["Orthomam_ID"].astype(str)
relax_df["Gene"] = relax_df["Gene"].astype(str)

# Merge on Orthomam ID
merged_df = pd.merge(relax_df, gene_map, left_on="Gene", right_on="Orthomam_ID", how="left")

# Drop redundant column and rename if needed
merged_df = merged_df.drop(columns=["Orthomam_ID"])  # optional
# Save to file
merged_df.to_csv("Bmal-allgenes_relax_with_Kval-Pval_FDR_and_Symbol.tsv", sep="\t", index=False)

# Optional: print a few lines
print(merged_df.head())

