
import numpy as np
import os
import subprocess

precisions = np.arange(3,53)
elements = np.arange(10000,110000,10000) 

for elm in elements: 
    for prec in precisions:
        script_content =f"""#!/bin/bash
#SBATCH --job-name=RS_{prec}_{elm}_cross_sin
#SBATCH --account=hpc2n2023-144
#SBATCH --time=01:00:00
#SBATCH --ntasks=1
#SBATCH -C intel_cpu
ml gompi
ml verificarlo

export VFC_BACKENDS="libinterflop_vprec.so --precision-binary64={prec}"
srun ./reactor_simulator_vfc 0 1 1 {elm} > /home/g/ggedik/reaktor/all_precisions/RS_prec{prec}_elm{elm}.txt 
"""
        file_name=f"batch_prec{prec}_elem{elm}.bat"
        with open (file_name, 'w') as file:
            file.write(script_content)
