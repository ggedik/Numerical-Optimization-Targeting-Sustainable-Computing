import numpy as np
import os
import subprocess

double_usr = []
double_sys = []
mixed_usr = []
mixed_sys = []


mixed_median_arr =[]
mixed_mean_arr   =[]
mixed_std_arr    =[]
mixed_var_arr    =[]
mixed_tot_arr =[]
double_median_arr =[]
double_mean_arr   = []
double_std_arr    =[]
double_var_arr    = []
double_tot_arr = []

nb_elements = np.arange(10000,110000,10000)
for elm in nb_elements:
    double_usr =[]
    mixed_usr =[]
    mixed_sys =[]
    double_sys =[]
    for i in range (1,55):
        result =  subprocess.run(["/usr/bin/time","--format", "\"%U\n%S\"", "./reactor_simulator_double","1"," 1"," 1", f"{elm}"], stdout=subprocess.PIPE, stderr= subprocess.PIPE)
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

    for i in range (1,55):
        result =  subprocess.run(["/usr/bin/time","--format", "\"%U\n%S\"", "./reactor_simulator_single","1"," 1"," 1",f"{elm}"], stdout=subprocess.PIPE, stderr= subprocess.PIPE)
            #capture_output=True, text=True)
        output = result.stdout
        output_err = result.stderr.decode('utf-8')
         #.strip('\"').split('\\n'
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
    double_tot_arr.append(double_tot)
    mixed_tot_arr.append(mixed_tot)
    print(mixed_tot)
    print(double_tot)

    mixed_median = np.median(mixed_tot)
    mixed_median_arr.append(mixed_median)
    mixed_mean   = np.mean (mixed_tot)
    mixed_mean_arr.append(mixed_mean)
    mixed_std    = np.std(mixed_tot)
    mixed_std_arr.append(mixed_std)
    mixed_var    = np.var(mixed_tot)
    mixed_var_arr.append(mixed_var)

    print(f"Mixed Results : \n \
    Median:{mixed_median} \n \
    Mean:  {mixed_mean} \n \
    STD:   {mixed_std} \n \
    VAR:   {mixed_var} \n ")
    double_median = np.median(double_tot)
    double_median_arr.append(double_median)
    double_mean   = np.mean (double_tot)
    double_mean_arr.append(double_mean)
    double_std    = np.std(double_tot)
    double_std_arr.append(double_std)
    double_var    = np.var(double_tot)
    double_var_arr.append(double_var)

    print(f"Double Results : \n \
    Median:{double_median} \n  \
    Mean:  {double_mean} \n  \
    STD:   {double_std} \n \
    VAR:   {double_var} \n ")


    print(f"Median Saving : {np.abs(double_median - mixed_median)/np.abs(double_median)} \n")
    print(f"Mean Saving : {np.abs(double_mean - mixed_mean) / np.abs(double_mean)} \n")

print("double array: ", double_tot_arr)
print("mixed array : ", mixed_tot_arr)
file_name = "double_mean_arr.txt"
with open(file_name,'w') as file:
    file.write(double_mean_arr)
file_name = "double_median_arr.txt"
with open(file_name,'w') as file:
    file.write(double_median_arr)
file_name = "double_std_arr.txt"
with open(file_name,'w') as file:
    file.write(double_std_arr)
file_name = "double_var_arr.txt"
with open(file_name,'w') as file:
    file.write(double_var_arr)
file_name = "double_mean_arr.txt"
with open(file_name,'w') as file:
    file.write(double_mean_arr)
file_name = "double_tot_arr.txt"
with open(file_name,'w') as file:
    file.write(double_tot_arr)
file_name = "mixed_std_arr.txt"
with open(file_name,'w') as file:
    file.write(mixed_std_arr)
file_name = "mixed_var_arr.txt"
with open(file_name,'w') as file:
    file.write(mixed_var_arr)
file_name = "mixed_mean_arr.txt"
with open(file_name,'w') as file:
    file.write(mixed_mean_arr)
file_name = "mixed_median_arr.txt"
with open(file_name,'w') as file:
    file.write(mixed_median_arr)
file_name = "mixed_tot_arr.txt"
with open(file_name,'w') as file:
    file.write(mixed_tot_arr)
