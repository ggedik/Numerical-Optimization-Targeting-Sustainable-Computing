#!/bin/bash                                                                                                                                      
#SBATCH --job-name=Reactor_FP32_functions                                                                                                                
#SBATCH --account=hpc2n2023-144                                                                                                                  
#SBATCH --ntasks=1                                                                                                                               
#SBATCH --time=00:30:00                                                                                                                          
#SBATCH --cpus-per-task=16                                                                                                                        
#SBATCH -C intel_cpu                                                                                                                             


module load foss
module load verificarlo

pip install numpy subprocess os sys threading multiprocessing
python3 par_script_functions.py





