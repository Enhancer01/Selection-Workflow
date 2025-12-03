import json
import glob
import os

output = []

for file in glob.glob("*.json"):
    try:
        with open(file, 'r') as f:
            data = json.load(f)

        # Navigate to test results → p-value
        pval = data.get("test results", {}).get("p-value", None)

        if pval is not None:
            gene_name = os.path.basename(file).replace("_fastgap.json", "")
            output.append((gene_name, pval))
        else:
            print(f"❌ No p-value in {file}")
    except Exception as e:
        print(f"⚠️ Error reading {file}: {e}")

# Write to file
with open("all_relax_pvalues_from_json.txt", "w") as out:
    for gene, pval in output:
        out.write(f"{gene}\t{pval}\n")

print(f"✅ Done: {len(output)} genes with p-values written to all_relax_pvalues_from_json.txt")

