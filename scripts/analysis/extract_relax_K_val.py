import os
import json
import csv

# Directory containing the RELAX JSON files
input_dir = "new_json_output"  # ✅ Confirm this is correct
output_file = "relax_k_values_summary.csv"

# Store results
results = []

# Traverse all JSON files
for filename in os.listdir(input_dir):
    if filename.endswith('.json'):
        filepath = os.path.join(input_dir, filename)
        with open(filepath, 'r') as f:
            try:
                data = json.load(f)
                branches = data.get("branch attributes", {}).get("0", {})
                for species, attrs in branches.items():
                    k_value = attrs.get("k (general descriptive)")
                    if k_value is not None:
                        results.append([species, k_value, filename])
            except (json.JSONDecodeError, KeyError) as e:
                print(f"❌ Error in {filename}: {e}")

# Write to CSV
with open(output_file, 'w', newline='') as out_csv:
    writer = csv.writer(out_csv)
    writer.writerow(["Species", "K-value", "SourceFile"])
    writer.writerows(results)

print(f"✅ Extracted {len(results)} K-values to {output_file}")

