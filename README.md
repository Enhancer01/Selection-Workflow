# Selection Workflow Project
#I actually need to be updating this acount often
#I push some of my work from my SSH to here, I would try and properly organize in later time though
#I also dont want to lose some of the files

## Script Categories

### 📊 Phylogenetic Analysis (scripts/phylo/)
- iqtree_parallel.sh - Parallel execution of IQ-TREE for phylogenetic inference
- cat_geneTree.sh - Concatenate and process gene trees
- prune-decimal-branchLength.py - Tree manipulation and branch length adjustment

### 🧬 Evolutionary Hypothesis Testing (scripts/evo-hypo/)
- runHyphy-parallel.sh - Main pipeline for running HyPhy analyses in parallel
- macse.sh - Multiple Alignment of Coding SEquences preparation
- traccer_script.sh - TRACCER (Tree Analysis for Convergent Evolution) pipeline

### 📈 Data Analysis (scripts/analysis/)
- extract_p-val_json2.py - Extract p-values from JSON format results
- extract_relax_K_val.py - Extract and process RELAX K-values
- opposingGene_plt.py - Generate plots for opposing gene selection analysis
- script_add_geneID.py - Add gene identifiers to analysis results
- script_adj_pval.py - Adjust p-values for multiple testing correction
- script_calculate_avg_K-val_perSpecies_relax.py - Calculate average K-values per species
- TRACCER.py - Main TRACCER analysis implementation

## Code Collection

The code_dump file contains frequently used code snippets and commands for evolutionary analysis. This serves as a quick reference and saves time when setting up new analyses.

## Usage

1. Clone the repository:
   bash
   git clone git@github.com:Enhancer01/Selection-Workflow.git
