#!/bin/bash                                                                                                                                      
#SBATCH --job-name=lulesh_VC_FP32_functions                                                                                                                
#SBATCH --account=hpc2n2023-144                                                                                                                  
#SBATCH --ntasks=1                                                                                                                               
#SBATCH --time=23:00:00                                                                                                                          
#SBATCH --cpus-per-task=16                                                                                                                        
#SBATCH -C intel_cpu                                                                                                                             



pip install numpy subprocess os sys threading multiprocessing
python3 par_script_functions.py





