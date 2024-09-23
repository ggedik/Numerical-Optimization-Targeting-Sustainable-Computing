import os
import numpy as np

#precisions = np.arange(3,53)
#precisions = [40,80,100,125,150]
nb_elems = np.arange (5,55,5)
for prec in nb_elems:
    os.system(f"sbatch batch_elm{prec}.bat")
