#!/bin/bash

username=`whoami`

stuff=$(squeue -l -u $username)

jr=$(echo $stuff | grep RUNNING | wc -l)
echo "jobs running: $jr"
jp=$(echo $stuff | grep PENDING | wc -l)
echo "jobs pending: $jp"
js=$(echo $stuff | grep SUSP | wc -l)
echo "jobs suspended: $js"
tot=$(echo $stuff | awk 'NR>1 {print $1}' |wc -l)
echo "Total jobs: $tot"
