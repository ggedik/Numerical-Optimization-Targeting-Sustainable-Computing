
import numpy as np
import os
import subprocess

precisions = np.arange(3,53)
elements = np.arange(10000,60000,10000) 
for prec in precisions:
    os.system (f"cp output.txt output_prec{prec}.txt")
    os.system(f"python3 set_input_file.py output_prec{prec}.txt {prec} 11 23 8 cross/sin ")
for elm in elements: 
    for prec in precisions:
        script_content =f"""#!/bin/bash
#SBATCH --job-name=RS_{prec}_{elm}_cross_sin
#SBATCH --account=hpc2n2023-144
#SBATCH --time=00:30:00
#SBATCH --ntasks=1
#SBATCH -C intel_cpu
ml gompi
ml verificarlo

export VFC_BACKENDS="libinterflop_vprec.so --prec-input-file=output_prec{prec}.txt --instrument=all"
srun ./reactor_simulator_vfc 0 1 1 {elm} > /home/g/ggedik/reaktor/sin_precisions/nb_elements/RS_cross_sin_prec{prec}_elm{elm}.txt 
echo $VFC_BACKENDS >> /home/g/ggedik/reaktor/sin_precisions/nb_elements/RS_cross_sin_prec{prec}_elm{elm}.txt
"""
        file_name=f"batch_prec{prec}_elem{elm}.bat"
        with open (file_name, 'w') as file:
            file.write(script_content)
