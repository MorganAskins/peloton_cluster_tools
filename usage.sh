#!/bin/bash -l
#SBATCH -t 10:00

srun -t 10:00 du -ch -d 0 * > usage.txt
