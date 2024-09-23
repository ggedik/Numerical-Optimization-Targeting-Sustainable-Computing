import numpy as np
import multiprocessing as mp
import sys 
import os 
import threading 
import subprocess
import string


src_func_names = [
"TimeIncrement",   
"InitStressTermsForElems" , 
"CalcElemShapeFunctionDerivatives" ,
"SumElemFaceNormal" , 
"CalcElemNodeNormals" ,
"SumElemStressesToNodeForces", 
"IntegrateStressForElems", 
"CollectDomainNodesToElemNodes",
"VoluDer",
"CalcElemVolumeDerivative",
"CalcElemFBHourglassForce",
"CalcFBHourglassForceForElems", 
"CalcHourglassControlForElems",
"CalcVolumeForceForElems",
"CalcForceForNodes",
"CalcAccelerationForNodes", 
"ApplyAccelerationBoundaryConditionsForNodes",
"CalcVelocityForNodes",
"CalcPositionForNodes", 
"LagrangeNodal",
"CalcElemVolume",
"AreaFace" , 
"CalcElemCharacteristicLength",
"CalcElemVelocityGrandient", 
"CalcKinematicsForElems", 
"CalcLagrangeElements", 
"CalcMonotonicQGradientsForElems",
"CalcMonotonicQRegionForElems", 
"CalcMonotonicQForElems", 
"CalcQForElems",
"CalcPressureForElems",
"CalcEnergyForElems",
"CalcSoundSpeedForElems",
"EvalEOSForElems", 
"ApplyMaterialPropertiesForElems",
"UpdateVolumesForElems",
"LagrangeElements",
"CalcCourantConstraintForElems", 
"CalcHydroConstraintForElems"]
print(len(src_func_names))
src_func_names = np.unique(src_func_names)
print(len(src_func_names))

order = 0 
def find_word(nb):

    return

def search_word_in_third_column(file_path, search_word):
    results = []
    with open(file_path, 'r') as file:
        for line in file:
            columns = line.split()
            #print(len(columns))
            if len(columns) == 3 and search_word in columns[2]:
            
            #results.append(line.strip())
               # results.append(columns[2])
                results = columns[2]
    return results
matching_lines = []
file_path = './function_names.txt'


for word in src_func_names: 
    matching_lines.append(search_word_in_third_column(file_path, word))

print(matching_lines)


def execute_parallel(program_name, system_call, elements, original_output):
    print(program_name)
    with open(original_output, "w") as file:
        result = subprocess.run(f"{system_call} ./functions_executables/{program_name} -s {elements} -p", shell=True, stdout=file,stderr=subprocess.PIPE, timeout=900)
    if result.returncode != 0:
           print(f"Error executing system call: {result.stderr.decode('utf-8')}")
    else:
        print(f"System call executed successfully, output written to {file}")

    return


precision = 23
elements = 10
threads = []
vprec_lib = "libinterflop_vprec.so"
system_call = f"VFC_BACKENDS=\"{vprec_lib} --precision-binary64={precision}\"" 
matching_lines.append("_ZL24CalcElemVelocityGradientPKdS0_S0_PA8_S_dPd")
for name in matching_lines:
    if (name == '[]'):
        skip
        
    program_name = f"lulesh_{name}"
    program_output = f"lulesh_{name}_{precision}_nb_{elements}.txt"
    func_comp    = f"cmake -DWITH_MPI=False -DCMAKE_VERBOSE_MAKEFILE=ON -DCMAKE_CXX_COMPILER=verificarlo-c++ -DCMAKE_CXX_FLAGS=\"--function=\"{name}\"\" -DLULESH_EXEC=\"lulesh_{name}\" .."
    
    result = subprocess.run(func_comp, shell=True)
    result = subprocess.run("make", shell=True)

    if result.returncode != 0:
        print(f"Error executing compile call: {result.stderr.decode('utf-8')}")
    else:
        print(f"System call executed successfully")
    thread = threading.Thread(target=execute_parallel, args = ( program_name , system_call, elements, program_output) )
    threads.append(thread)
    thread.start()


for thread in threads:
    thread.join()


    
