
import  numpy as np
import os
import subprocess

precisions = np.arange(3,53)

# for prec in precisions:
#     os.system (f"cp output.txt output_prec{}.txt ", shell=True)

for prec in precisions:
    script_content =f"""#!/bin/bash
#SBATCH --job-name=RS_{prec}cross_sin
#SBATCH --account=hpc2n2023-144
#SBATCH --time=00:30:00
#SBATCH --ntasks=1

export VFC_BACKENDS="libinterflop_vprec.so --prec-input-file=output_prec{prec}.txt --instrument=all --prec-log-file=log_file_{prec}.txt"
srun ./reactor_simulator_vfc 0 1 1 10000 > RS_cross_sin_prec{prec}.txt
"""
    file_name=f"batch_prec{prec}.bat"
    with open (file_name, 'w') as file:
        file.write(script_content)
