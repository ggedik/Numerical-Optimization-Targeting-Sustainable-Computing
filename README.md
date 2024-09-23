# Numerical Optimization Targeting Sustainable Scientific Computing

This repo contains some of the source files for my end-of-studies internship report/master's thesis at Umea University in Division of Computing Science under the supervision of Roman Iakymchuk and co-supervision of Pablo de Oliveira Castro, as part of my M.Sc. in High Performance Computing and Simulation at Paris-Saclay University, UVSQ.<br>
The source codes of the benchmarks, along with their mixed precision implementations done in this work are not included in this repository. The details regarding mixed precision implementations are given in the report.<br>
This repository provides support for computer arithmetic tools, i.e Verificarlo. Some scripts may require minor adjustments, such as updating file paths and other configurations.<br>

## Structure

.<br>
├── energy			: Directory containing scripts related to energy measurements.<br>
│   ├── measure_energy.py	: Script for measuring energy consumption using specific tools.<br>
│   └── process_measurements.py	: Script for processing and analyzing the collected energy measurement data.<br>
├── make_animation.ipynb	: Jupyter Notebook used for creating animations related to Reactor Simulator.<br>
├── presentation_GEDIK.pdf	: Presentation of the project, summarizing the research outcomes.<br>
├── README.md			: Main README file.<br>
└── vfc				: Directory containing work related to Verificarlo. Finding minimal precision for code regions, doing MCA analysis.<br> 
    ├── LULESH			: Folder dedicated to the LULESH application, containing scripts.<br>
    └── REACTOR_SIMULATOR	: Folder dedicated to the Reactor Simulator, containing scripts.<br>
## Requirements
In order to be able to replicate the results obtained in this research you must have:

1. Compilers:

   This project heavily relies on [Verificarlo version 1.0.0](https://github.com/verificarlo). Please check the documentation.
   
   On Kebnekaise, we use g++ version 10.2, on Laptop we use g++ version 11.4.0.

   Both with Verificarlo and GNU Compilers, everything is compiled with -O2 optimization flag.
 
2. Use Cases:
   The LULESH use case is using [version 2.0](https://github.com/LLNL/LULESH). And more information about LULESH is available [here](https://asc.llnl.gov/codes/proxy-apps/lulesh).

   Detailed information on the Reactor Simulator and the code is available in [here](https://people.math.sc.edu/Burkardt/cpp_src/reactor_simulation/reactor_simulation.html), C++ version is used in our experiments.

3. Reproducing Graphs:
   We used Python to produce the graphs and analyze the results.
   Remember: reporducing *exactly* the same results as in this study is a challange. But if you want to try anyway, detailed information about the systems is given in the report.

4. Energy Measurements:
   Most of the time they require elevated privileges. Because of this, in this work we used a custom tool to take the measurements on our personal system. The tool is not hosted in this repository. 

## Key Findings:
Through case studies on the Reactor Simulator and LULESH benchmarks, we demonstrated
that applying mixed-precision strategies can lead to significant reductions in both time-to-
solution and energy-to-solution, sometimes without sacrificing accuracy. Our findings show a
15% reduction in both metrics without any compromise on accuracy, for the Reactor Simulator
and up to a 20% improvement in time-to-solution and a 10% reduction in energy-to-solution
for the LULESH benchmark. These results highlight the importance of adopting ‘just enough
precision’ to optimize performance and energy use in scientific computing.

## Contact :
If you have any questions, or want to let us know about your results please do not hesitate to get in  contact at this mail:
ggedik@cs.umu.se


## Some Notes:
- [nm](https://www.man7.org/linux/man-pages/man1/nm.1.html) is used to get the mangled function names.
- [Callgrind](https://valgrind.org/docs/manual/cl-manual.html) is used to detect hotspots.
- Callgrid output then turned to graphs with the help of [graph2dot](https://github.com/jrfonseca/gprof2dot).
- [Intel Advisor Roofline](https://www.intel.com/content/www/us/en/developer/articles/guide/intel-advisor-roofline.html) is used to generate the data points for Roofline graphs. 
- [Rooflini](https://github.com/giopaglia/rooflini) is used to represent the Roofline graphs esthetically. 
