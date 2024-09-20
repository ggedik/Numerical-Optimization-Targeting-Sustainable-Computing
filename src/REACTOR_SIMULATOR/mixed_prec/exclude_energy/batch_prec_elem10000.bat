#!/bin/bash
#SBATCH --job-name=RS_10000
#SBATCH --account=hpc2n2023-144
#SBATCH --time=01:00:00
#SBATCH --ntasks=1
#SBATCH -C intel_cpu


ml foss

srun ./reactor_simulator_double 0 1 1 10000 > /home/g/ggedik/reaktor/mixed_prec/change_funcs/RS_double_10000.txt
srun ./reactor_simulator_mixed_prec_full_funcs_v3 0 1 1 10000 > /home/g/ggedik/reaktor/mixed_prec/change_funcs/RS_v3_elm10000.txt 
