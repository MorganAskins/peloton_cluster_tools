username=`whoami`
jobcount=`squeue -l -u $username -t SUSPENDED | grep SUSPEND | awk '{print $1}' | wc -l`
echo "Suspended jobs: $jobcount"
jobset=`squeue -l -u $username -t SUSPENDED | awk 'FNR>2 {ORS=","} {print $1}' | awk 'FNR>2 {print $1}'`
if [[ $jobcount -gt 0 ]];
then
  scontrol requeue $jobset
fi
