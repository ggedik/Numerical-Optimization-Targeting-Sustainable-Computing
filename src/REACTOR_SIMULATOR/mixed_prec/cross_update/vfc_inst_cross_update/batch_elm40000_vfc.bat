#!/bin/bash
#SBATCH --job-name=RS_23cross_sin
#SBATCH --account=hpc2n2023-144
#SBATCH --time=00:30:00
#SBATCH --ntasks=1

ml foss
ml verificarlo
export VFC_BACKENDS="libinterflop_vprec.so --precision-binary64=23"
srun ./reactor_simulator_double_cross_update_vfc 0 1 1 40000 > ./RS_cross_update_vfc_prec23_elm40000.txt 
