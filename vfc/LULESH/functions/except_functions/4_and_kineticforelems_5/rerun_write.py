import subprocess
import sys
import numpy as np
import os
import subprocess

precisions = np.arange(5,55,5)
its = [128, 300, 476, 670, 820, 1020,1200,1400,1550,1750,1900]
myit = 0 
for i in precisions:
    script_content =f"""#!/bin/bash
#SBATCH --job-name=rerun_lulesh2
#SBATCH --account=hpc2n2023-144
#SBATCH --time=20:00:00
#SBATCH --ntasks=1
#SBATCH -C intel_cpu


export VFC_BACKENDS="libinterflop_vprec.so --precision-binary64=23"
python3 cut_off.py ./build/lulesh_except_5 -s {i} -p  {its[myit]} lulesh_except_time_elm{i}.txt
"""
    myit=myit+1
    file_name=f"batch_elm{i}.bat"
    with open (file_name, 'w') as file:
        file.write(script_content)
