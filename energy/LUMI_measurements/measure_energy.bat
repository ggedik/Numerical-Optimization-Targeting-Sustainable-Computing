#!/bin/bash                                                                                                                                       

#SBATCH -A                                                                                                                       
#SBATCH -N 1                                                                                                                                      
#SBATCH --partition small                                                                                                                         
#SBATCH --exclusive                                                                                                                               
#SBATCH --time=01:00:00                                                                                                                           


for ((i=1;i<33;i++)) do

srun ./build/luleshv2_stage1 -s 20 -q
done




