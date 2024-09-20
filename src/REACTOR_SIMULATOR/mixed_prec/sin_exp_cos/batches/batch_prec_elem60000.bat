#!/bin/bash
#SBATCH --job-name=RS_60000
#SBATCH --account=hpc2n2023-144
#SBATCH --time=01:00:00
#SBATCH --ntasks=1
#SBATCH -C intel_cpu


ml foss

srun ./reactor_simulator_double 0 1 1 60000 > ./RS_double_60000.txt
srun ./reactor_simulator_sinf_expf_cosf 0 1 1 60000 > ./RS_sinf_expf_cosf_elm60000.txt 
