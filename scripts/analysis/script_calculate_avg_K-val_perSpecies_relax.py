import pandas as pd

# Load the input file (whitespace-delimited)
df = pd.read_csv("Combined_Kval_relax.txt", sep="\s+", engine='python')

# Group by Species and compute the mean K-value
avg_df = df.groupby("Species", as_index=False)["K-value"].mean()

# Rename column for clarity
avg_df.rename(columns={"K-value": "average_K-value"}, inplace=True)

# Save to output file
avg_df.to_csv("Average_Kval_per_species.tsv", sep="\t", index=False)

# Optional: preview first few rows
print(avg_df.head())

