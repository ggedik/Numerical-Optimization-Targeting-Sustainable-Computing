import subprocess
import sys
import numpy as np
import os
import subprocess

precisions = np.arange(1,36)
for i in precisions:
    script_content =f"""#!/bin/bash
#SBATCH --job-name=mca_lulesh2
#SBATCH --account=hpc2n2023-144
#SBATCH --time=3:00:00
#SBATCH --ntasks=1
#SBATCH -C intel_cpu


export VFC_BACKENDS="libinterflop_mca.so --mode=mca --precision-binary64=23"
python3 cut_off.py /home/g/ggedik/luleshv2/luleshv2_serial_build/luleshv2_vfc/build/lulesh2.0 -s 20 -p  630 /home/g/ggedik/luleshv2/luleshv2_serial_build/luleshv2_vfc/mca_backend/mca_mode/fp32_inst/results/mca_fp32_luleshv2_run{i}.txt 
"""
    file_name=f"batch_run{i}.bat"
    with open (file_name, 'w') as file:
        file.write(script_content)
