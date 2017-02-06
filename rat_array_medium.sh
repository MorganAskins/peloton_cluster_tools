#!/bin/bash -l
#SBATCH -t 1-00:00
#SBATCH -p med

# The use of SLURM_ARRAY_TASK_ID is useful for running
# a single macro many times. Example usage:
# for f in *.mac;
# do
#   sbatch --array=1-100%10 ./rat_array_medium.sh $f
#   sleep 0.1
# done
# The %10 tells slurm to only run 10 jobs at a time

srun rat $1 -o $1_${SLURM_ARRAY_TASK_ID}.root
