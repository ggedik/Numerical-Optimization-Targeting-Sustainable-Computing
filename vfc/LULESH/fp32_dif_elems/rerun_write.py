import subprocess
import sys
import numpy as np
import os
import subprocess

#precisions = np.arange(3,53)
nb_elems = np.arange(5,55,5)
for i in nb_elems:
    script_content =f"""#!/bin/bash
#SBATCH --job-name=rerun_lulesh2
#SBATCH --account=hpc2n2023-144
#SBATCH --time=2:00:00
#SBATCH --ntasks=1
#SBATCH -C intel_cpu


export VFC_BACKENDS="libinterflop_vprec.so --precision-binary64=23"
python3 cut_off.py /home/g/ggedik/luleshv2/luleshv2_serial_build/luleshv2_vfc/build/lulesh2.0 -s {i} -p 1750 /home/g/ggedik/luleshv2/luleshv2_serial_build/luleshv2_vfc/fp32_dif_elems/lulesh_prec23_elm{i}.txt
"""
    file_name=f"batch_elm{i}.bat"
    with open (file_name, 'w') as file:
        file.write(script_content)
