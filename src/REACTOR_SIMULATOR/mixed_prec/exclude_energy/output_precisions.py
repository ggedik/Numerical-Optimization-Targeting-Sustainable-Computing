
import numpy as np
import os
import subprocess

precisions = np.arange(3,53)
elements = np.arange(10000,110000,10000) 
#for prec in precisions:
#    os.system (f"cp output.txt output_prec{prec}.txt")
#    os.system(f"python3 set_input_file.py output_prec{prec}.txt {prec} 11 23 8 cross/sin ")
for elm in elements: 
    #for prec in precisions:
        script_content =f"""#!/bin/bash
#SBATCH --job-name=RS_{elm}
#SBATCH --account=hpc2n2023-144
#SBATCH --time=01:00:00
#SBATCH --ntasks=1
#SBATCH -C intel_cpu


ml foss

srun ./reactor_simulator_double 0 1 1 {elm} > /home/g/ggedik/reaktor/mixed_prec/change_funcs/RS_double_{elm}.txt
srun ./reactor_simulator_mixed_prec_full_funcs_v3 0 1 1 {elm} > /home/g/ggedik/reaktor/mixed_prec/change_funcs/RS_v3_elm{elm}.txt 
"""
        file_name=f"batch_prec_elem{elm}.bat"
        with open (file_name, 'w') as file:
            file.write(script_content)
