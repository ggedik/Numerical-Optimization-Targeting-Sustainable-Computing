import os
import numpy as np

#precisions = np.arange(3,53)
elements = np.arange(10000,110000,10000)
#for prec in precisions:
for elm in elements:
        os.system(f"sbatch batch_exc_s_e_elm{elm}.bat")
