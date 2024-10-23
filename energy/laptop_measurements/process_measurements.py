import os
import csv
import numpy as np 

parent_dir = "."

sum_cores = []
sum_gpu = []
sum_pkg = []
sum_psys = []

count_cores = []
count_gpu = []
count_pkg = []
count_psys = []


def process_csv(file_path):
    total_sum = 0
    count = 0
    
    with open(file_path, 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=";")
        
        for row in reader:
            row_sum = sum(float(value) for value in row if value)  # Only sum non-empty values
            total_sum += row_sum
            count += len(row) 
    
    return total_sum, count


for i in range(32):
    folder_name = f"folder_{i+1}"
    folder_path = os.path.join(parent_dir, folder_name)

    
    cores_sum, cores_count = process_csv(os.path.join(folder_path, "energy-cores.csv"))
    sum_cores.append(cores_sum)
    count_cores.append(cores_count)

    
    gpu_sum, gpu_count = process_csv(os.path.join(folder_path, "energy-gpu.csv"))
    sum_gpu.append(gpu_sum)
    count_gpu.append(gpu_count)

   
    pkg_sum, pkg_count = process_csv(os.path.join(folder_path, "energy-pkg.csv"))
    sum_pkg.append(pkg_sum)
    count_pkg.append(pkg_count)

   
    psys_sum, psys_count = process_csv(os.path.join(folder_path, "energy-psys.csv"))
    sum_psys.append(psys_sum)
    count_psys.append(psys_count)


print("Sum of energy-cores.csv for each folder:", sum_cores)
print("Number of elements in energy-cores.csv for each folder:", count_cores)
print("Sum of energy-gpu.csv for each folder:", sum_gpu)
print("Number of elements in energy-gpu.csv for each folder:", count_gpu)
print("Sum of energy-pkg.csv for each folder:", sum_pkg)
print("Number of elements in energy-pkg.csv for each folder:", count_pkg)
print("Sum of energy-psys.csv for each folder:", sum_psys)
print("Number of elements in energy-psys.csv for each folder:", count_psys)
# Calculate the arrays that divide the sum by the corresponding number of measurements
mean_cores = [sum_val  if count_val != 0 else 0 for sum_val, count_val in zip(sum_cores, count_cores)]
mean_gpu = [sum_val  if count_val != 0 else 0 for sum_val, count_val in zip(sum_gpu, count_gpu)]
mean_pkg = [sum_val  if count_val != 0 else 0 for sum_val, count_val in zip(sum_pkg, count_pkg)]
mean_psys = [sum_val  if count_val != 0 else 0 for sum_val, count_val in zip(sum_psys, count_psys)]


print("Mean of energy-cores.csv for each folder:", mean_cores)
print("Mean of energy-gpu.csv for each folder:", mean_gpu)
print("Mean of energy-pkg.csv for each folder:", mean_pkg)
print("Mean of energy-psys.csv for each folder:", mean_psys)


def print_statistics(data, label):
    print(f"\nStatistics for {label}:")
    print(f"Mean: {np.mean(data)}")
    print(f"Median: {np.median(data)}")
    print(f"Standard Deviation: {np.std(data)}")
    print(f"Variance: {np.var(data)}")


print_statistics(mean_cores, "Mean Cores")
print_statistics(mean_gpu, "Mean GPU")
print_statistics(mean_pkg, "Mean Package")
print_statistics(mean_psys, "Mean PSYS")

# Calculate statistics for the first 10 folders
mean_cores_first_10 = mean_cores[:10]
mean_gpu_first_10 = mean_gpu[:10]
mean_pkg_first_10 = mean_pkg[:10]
mean_psys_first_10 = mean_psys[:10]

# Print statistics for the first 10 folders
print_statistics(mean_cores_first_10, "Mean Cores (First 10 Folders)")
print_statistics(mean_gpu_first_10, "Mean GPU (First 10 Folders)")
print_statistics(mean_pkg_first_10, "Mean Package (First 10 Folders)")
print_statistics(mean_psys_first_10, "Mean PSYS (First 10 Folders)")
