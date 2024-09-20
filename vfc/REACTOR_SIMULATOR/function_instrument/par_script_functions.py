import numpy as np
import multiprocessing as mp
import sys 
import os 
import threading 
import subprocess
import string


src_func_names = [
    "absorb",
    "cross",
    "dist2c",
    "energy",
    "r8_max",
    "r8_abs",
    "r8_uniform_01",
    "scatter",
    "source",
    "update"]
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
file_path = './reactor_simulator_function_names.txt'


for word in src_func_names: 
    matching_lines.append(search_word_in_third_column(file_path, word))

print(matching_lines)

elements_list1 = np.arange(10, 110, 10)
elements_list1 = list(elements_list1)
elements_list1.append(125)
[elements_list1.append(x) for x in np.arange (150, 1050, 50)]
#print(elements_list1)

def execute_parallel(program_name, system_call, elements, original_output):
    print(program_name)
    with open(original_output, "w") as file:
        result = subprocess.run(f"{system_call} ./{program_name} 0 1 1 {elements}", shell=True, stdout=file,stderr=subprocess.PIPE, timeout=6600)
    if result.returncode != 0:
           print(f"Error executing system call: {result.stderr.decode('utf-8')}")
    else:
        print(f"System call executed successfully, output written to {file}")

    return

#elements_list1=matching_lines

precision = 23
elements = 10000 
threads = []
vprec_lib = "libinterflop_vprec.so"
system_call = f"VFC_BACKENDS=\"{vprec_lib} --precision-binary64={precision}\"" 

for name in matching_lines:
    
    program_name = f"reactor_simulator"
    program_output = f"RS_{name}_{precision}_nb_{elements}.txt"
    func_comp    = f" verificarlo-c++ reactor_simulator.cpp -o {program_name}_vfc_{name} --function {name} "
    
    result = subprocess.run(func_comp, shell=True)
    if result.returncode != 0:
        print(f"Error executing compile call: {result.stderr.decode('utf-8')}")
    else:
        print(f"System call executed successfully")
    thread = threading.Thread(target=execute_parallel, args = ( program_name , system_call, elements, program_output) )
    threads.append(thread)
    thread.start()


for thread in threads:
    thread.join()


    
