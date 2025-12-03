python -c "import sys, re; print(re.sub(r':(\d+\.\d{4})\d*', r':\1', sys.stdin.read()))" < your_tree.nwk > rounded_tree.nwk

#to prune a tree
for f in *txt; do nw_prune rounded_new_ellsm-timetree.nwk -v -f "$f" > "${f%%txt}tree2"; done
