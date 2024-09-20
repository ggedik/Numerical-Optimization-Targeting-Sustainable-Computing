
import  numpy as np
import os
import subprocess

precisions = np.arange(10000,110000,10000)

# for prec in precisions:
#     os.system (f"cp output.txt output_prec{}.txt ", shell=True)

for elm in precisions:
    script_content =f"""#!/bin/bash
#SBATCH --job-name=RS_23cross_sin
#SBATCH --account=hpc2n2023-144
#SBATCH --time=00:30:00
#SBATCH --ntasks=1

ml foss


srun ./reactor_simulator_double_cross_update 0 1 1 {elm} > ./RS_double_cross_update_prec23_elm{elm}.txt 
"""
    file_name=f"batch_elm{elm}.bat"
    with open (file_name, 'w') as file:
        file.write(script_content)
