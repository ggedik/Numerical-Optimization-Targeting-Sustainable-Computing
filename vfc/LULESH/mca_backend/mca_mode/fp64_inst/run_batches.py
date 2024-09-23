import os
import numpy as np

precisions = np.arange(1,36)
#precisions = [40,80,100,125,150]
for prec in precisions:
    os.system(f"sbatch batch_run{prec}.bat")
