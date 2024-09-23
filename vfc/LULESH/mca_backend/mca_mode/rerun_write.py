import subprocess
import sys
import numpy as np
import os
import subprocess

precisions = np.arange(3,53)
for i in precisions:
    script_content =f"""#!/bin/bash
#SBATCH --job-name=rerun_lulesh2
#SBATCH --account=hpc2n2023-144
#SBATCH --time=1:00:00
#SBATCH --ntasks=1
#SBATCH -C intel_cpu


export VFC_BACKENDS="libinterflop_vprec.so --precision-binary64={i}"
python3 cut_off.py /home/g/ggedik/luleshv2/luleshv2_serial_build/luleshv2_vfc/build/lulesh2.0 -s 10 -p  307 /home/g/ggedik/luleshv2/luleshv2_serial_build/luleshv2_vfc/precisions/results/lulesh_prec{i}_elm10.txt
"""
    file_name=f"batch_prec{i}.bat"
    with open (file_name, 'w') as file:
        file.write(script_content)
