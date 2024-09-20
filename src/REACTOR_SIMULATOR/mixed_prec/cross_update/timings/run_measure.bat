#!/bin/bash
#SBATCH --account=hpc2n2023-144
#SBATCH --time=01:00:00
#SBATCH -C intel_cpu
#SBATCH --exclusive

ml foss

python3 measure_time_double_cross_update.py
