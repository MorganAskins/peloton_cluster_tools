#!/bin/bash

username=`whoami`

jr=$(squeue -l -u $username | grep RUNNING | wc -l)
echo "jobs running: $jr"
jp=$(squeue -l -u $username | grep PENDING | wc -l)
echo "jobs pending: $jp"
js=$(squeue -l -u $username | grep SUSP | wc -l)
echo "jobs suspended: $js"
tot=$(squeue -l -u $username | awk 'NR>2 {print $1}' | wc -l)
echo "Total jobs: $tot"
