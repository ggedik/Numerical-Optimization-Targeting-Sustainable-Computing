#!/bin/bash                                                                                                                                                                                                                                                                                           

# Check if a job ID is provided                                                                                                                                                                                                                                                                       
if [ -z "$1" ]; then
    echo "Usage: $0 <job_id>"
    exit 1
fi

JOB_ID=$1
OUTPUT_FILE="job_${JOB_ID}_details.txt"
ENERGY_VALUES=()

# Header for the output file                                                                                                                                                                                                                                                                          
echo "Job ID, Step ID, Energy Consumption (Joules), Step Time, Job Time" > $OUTPUT_FILE

# Get the job information and append it to the file                                                                                                                                                                                                                                                   
sacct -j $JOB_ID --format=JobID,JobName,Elapsed,State,ConsumedEnergy --parsable2 | while IFS="|" read -r jobid jobname elapsed state energy; do
    if [ "$jobid" != "JobID" ]; then
        # Convert energy if it's in kilojoules (remove 'K' and multiply by 1000)                                                                                                                                                                                                                      
        if [[ "$energy" == *K ]]; then
           # echo "$energy" | sed 's/K//' | awk '{print $1 * 1000}'                                                                                                                                                                                                                                   
            energy=$(echo "$energy" | sed 's/K//' | awk '{print $1 * 1000}')
        fi

        # Add the energy to the list for median and mean calculation                                                                                                                                                                                                                                  
        ENERGY_VALUES+=($energy)
#       echo "$energy"                                                                                                                                                                                                                                                                                
        # Append job and step information to the output file                                                                                                                                                                                                                                          
        echo "$jobid, $jobname, $energy, $elapsed" >> $OUTPUT_FILE
    fi
done
