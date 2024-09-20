#!/bin/bash
#SBATCH --account=hpc2n2023-144
#SBATCH --time=01:00:00
#SBATCH -C intel_cpu
#SBATCH --exclusive

ml foss
ml verificarlo
python3 mesure_time_double_v3.py
