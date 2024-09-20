#!/bin/bash
#SBATCH --job-name=RS_23cross_sin
#SBATCH --account=hpc2n2023-144
#SBATCH --time=00:30:00
#SBATCH --ntasks=1

ml foss


srun ./reactor_simulator_exc_scatter_energy 0 1 1 50000 > ./RS_exc_scatter_energy_prec23_elm50000.txt 
