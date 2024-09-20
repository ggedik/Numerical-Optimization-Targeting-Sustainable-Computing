
import  numpy as np
import os
import subprocess

precisions = np.arange(3,53)

for prec in precisions:
    os.system (f"cp output.txt output_prec{prec}.txt")

for prec in precisions:
    os.system (f"python3 set_input_file.py output_prec{prec}.txt  {prec} 11 23 8 cross/exp")

for prec in precisions:
    script_content =f"""#!/bin/bash
#SBATCH --job-name=RS_{prec}cross_exp
#SBATCH --account=hpc2n2023-144
#SBATCH --time=00:30:00
#SBATCH --ntasks=1
#SBATCH -C intel_cpu

ml gompi 
ml verificarlo 
export VFC_BACKENDS="libinterflop_vprec.so --prec-input-file=output_prec{prec}.txt --instrument=all --prec-log-file=log_file_{prec}.txt"
srun ./reactor_simulator_vfc 0 1 1 10000 >  /home/g/ggedik/reaktor/exp_precisions/RS_cross_exp_prec{prec}.txt
echo $VFC_BACKENDS >> /home/g/ggedik/reaktor/exp_precisions/RS_cross_exp_prec{prec}.txt
"""
    file_name=f"batch_prec{prec}.bat"
    with open (file_name, 'w') as file:
        file.write(script_content)
