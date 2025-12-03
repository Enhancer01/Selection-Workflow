import pandas as pd
from statsmodels.stats.multitest import multipletests

# Read the file (assuming it's space-separated or tab-separated)
df = pd.read_csv("ellsm-k-pval.txt", sep="\s+", header=None, names=["Gene", "P_value", "K_value"])

# Perform FDR correction (Benjamini-Hochberg)
_, fdr_corrected, _, _ = multipletests(df["P_value"], method='fdr_bh')

# Add the FDR column to the DataFrame
df["FDR_Adjusted_P"] = fdr_corrected

# Save to new file
df.to_csv("Ellsm-allgenes_relax_Pval-Kval_with_FDR.tsv", sep="\t", index=False)

# Optional: print top few rows
print(df.head())

