#!/bin/bash
#SBATCH --job-name=RS_23cross_sin
#SBATCH --account=hpc2n2023-144
#SBATCH --time=00:30:00
#SBATCH --ntasks=1

ml foss


srun ./reactor_simulator_double_cross_update 0 1 1 30000 > ./RS_double_cross_update_prec23_elm30000.txt 
