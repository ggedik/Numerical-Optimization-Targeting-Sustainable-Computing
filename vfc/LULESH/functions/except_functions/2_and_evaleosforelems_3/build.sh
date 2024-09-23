#!/bin/bash
mkdir build
cd build
#cmake -DWITH_MPI=False -DCMAKE_VERBOSE_MAKEFILE=ON -DCMAKE_CXX_COMPILER=g++ ..
cmake -DWITH_MPI=False -DCMAKE_VERBOSE_MAKEFILE=ON -DCMAKE_CXX_COMPILER=verificarlo-c++ -DCMAKE_CXX_FLAGS="--exclude-file=/home/g/ggedik/luleshv2/luleshv2_serial_build/luleshv2_vfc/functions/excepts/2_and_evaleosforelems_3/exclude.txt" -DLULESH_EXEC="lulesh_except_3" ..
make 
