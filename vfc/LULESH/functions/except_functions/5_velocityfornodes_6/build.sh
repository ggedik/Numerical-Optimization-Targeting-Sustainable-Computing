#!/bin/bash
mkdir build
cd build
cmake -DWITH_MPI=False -DCMAKE_VERBOSE_MAKEFILE=ON -DCMAKE_CXX_COMPILER=verificarlo-c++ -DCMAKE_CXX_FLAGS="--exclude-file=/home/g/ggedik/luleshv2/luleshv2_serial_build/luleshv2_vfc/functions/excepts/5_velocityfornodes_6/exclude.txt" -DLULESH_EXEC="lulesh_except_6" ..
make 
