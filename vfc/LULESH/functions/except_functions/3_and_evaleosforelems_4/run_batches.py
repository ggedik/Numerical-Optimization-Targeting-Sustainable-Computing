import os
import numpy as np

precisions = np.arange(5,55,5)
#precisions = [5,10,20,30,45,50,70,90]
for prec in precisions:
    os.system(f"sbatch batch_elm{prec}.bat")
