import os
import numpy as np

precisions = np.arange(3,53)
#precisions = [40,80,100,125,150]
for prec in precisions:
    os.system(f"sbatch batch_prec{prec}.bat")
