#!/bash
# Load Conda
source /home/otunde/yes/etc/profile.d/conda.sh
conda activate hyphy_env

# Export environment for use in GNU parallel
export PATH="$CONDA_PREFIX/bin:$PATH"

# Run HyPhy ABSREL jobs in parallel
nohup parallel -j 20 '
tree="{.}_sed.tree"
hyphy relax --alignment {} --tree "$tree" --test test_bw50kg --output "{.}.json"
' ::: *fa-gb > relaX_parallel.log 2>&1 &

