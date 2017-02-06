#!/bin/bash -l
#SBATCH -t 1-00:00
#SBATCH -p med

# To run rat over many macros in parallel do:
# for f in *.mac;
# do
#   sbatch rat_medium.sh $f;
#   sleep 0.1;
# done

srun rat $1
