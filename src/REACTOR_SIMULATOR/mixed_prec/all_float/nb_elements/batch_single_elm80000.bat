#!/bin/bash
#SBATCH --job-name=RS_23cross_sin
#SBATCH --account=hpc2n2023-144
#SBATCH --time=00:30:00
#SBATCH --ntasks=1

ml foss

srun ./reactor_simulator_double 0 1 1 80000 > ./RS_double_elm80000.txt
srun ./reactor_simulator_single 0 1 1 80000 > ./RS_single_prec23_elm80000.txt 
