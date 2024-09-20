import numpy as np
import os
import subprocess

double_usr = []
double_sys = []
mixed_usr = []
mixed_sys = []

for i in range (1,32):
    result =  subprocess.run(["/usr/bin/time","--format", "\"%U\n%S\"", "./reactor_simulator_double","1"," 1"," 1"," 5000000"], stdout=subprocess.PIPE, stderr= subprocess.PIPE)
    #capture_output=True, text=True)
    output = result.stdout
    output_err = result.stderr.decode('utf-8')
    #.strip('\"').split('\\n')
    cleaned = output_err.strip('"').split('\\n')   
    cleaned = output_err.strip('"').replace('\\n' , '\n').split('\n')
    #  print(output)
    #print(cleaned)
    cleaned = [s.strip('"') for s in cleaned if s.strip('"')]
    print (float(cleaned[0]))
    double_usr.append(float(cleaned[0]))
    double_sys.append(float(cleaned[1]))
    
#for i in range (1,32):
 #   subprocess.run("/usr/bin/time --format \"%U\n%S\" ./reactor_simulator_mixed_prec 1 1 1 5000000")
  #  mixed_time.append()

for i in range (1,32):
    result =  subprocess.run(["/usr/bin/time","--format", "\"%U\n%S\"", "./reactor_simulator_sinf_expf_cosf","1"," 1"," 1"," 5000000"], stdout=subprocess.PIPE, stderr= subprocess.PIPE)
    #capture_output=True, text=True)
    output = result.stdout
    output_err = result.stderr.decode('utf-8')
    #.strip('\"').split('\\n')
    cleaned = output_err.strip('"').split('\\n')   
    cleaned = output_err.strip('"').replace('\\n' , '\n').split('\n')
    #  print(output)
    #print(cleaned)
    cleaned = [s.strip('"') for s in cleaned if s.strip('"')]
    print (float(cleaned[0]))
    mixed_usr.append(float(cleaned[0]))
    mixed_sys.append(float(cleaned[1]))



mixed_tot = np.array (mixed_usr) + np.array (mixed_sys)
double_tot = np.array (double_usr) + np.array (double_sys)
print(mixed_tot)
print(double_tot)

mixed_median = np.median(mixed_tot)
mixed_mean   = np.mean (mixed_tot)
mixed_std    = np.std(mixed_tot)
mixed_var    = np.var(mixed_tot)

print(f"Mixed Results : \n \
Median:{mixed_median} \n \
Mean:  {mixed_mean} \n \
STD:   {mixed_std} \n \
VAR:   {mixed_var} \n ")
double_median = np.median(double_tot)
double_mean   = np.mean (double_tot)
double_std    = np.std(double_tot)
double_var    = np.var(double_tot)

print(f"Double Results : \n \
Median:{double_median} \n  \
Mean:  {double_mean} \n  \
STD:   {double_std} \n \
VAR:   {double_var} \n ")

print(f"Median Saving : {np.abs(double_median - mixed_median)/np.abs(double_median)} \n")
print(f"Mean Saving : {np.abs(double_mean - mixed_mean) / np.abs(double_mean)} \n")
