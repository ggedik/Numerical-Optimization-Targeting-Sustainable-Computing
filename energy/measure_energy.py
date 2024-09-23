import os
import subprocess


def execute_program(folder_path):
    
    command = ["/home/ggedik/internship/luleshv2/luleshv2_serial_build/luleshv2_orig/kernelstat", "fork", "5", "/home/ggedik/internship/luleshv2/luleshv2_serial_build/luleshv2_orig/build/lulesh2.0", "-s", "20", "-q"]

        
    subprocess.run(command)


parent_dir = "/home/ggedik/internship/luleshv2/luleshv2_serial_build/luleshv2_orig"


if not os.path.exists(parent_dir):
    os.makedirs(parent_dir)


for i in range(32):
    folder_name = f"folder_{i+1}"
    folder_path = os.path.join(parent_dir, folder_name)


    os.makedirs(folder_path, exist_ok=True)


    os.chdir(folder_path)


    execute_program(folder_path)


    os.chdir("..")

print("All folders created and programs executed successfully.")
