# Numerical Optimization Targeting Sustainable Scientific Computing

This repo contains the source files for my end-of-studies internship report/master's thesis at Umea University in Division of Computing Science under the supervision of Roman Iakymchuk and co-supervision of Pablo de Oliveira Castro, as part of my M.Sc. in High Performance Computing and Simulation at Paris-Saclay University, UVSQ.

## Requirements
In order to be able to replicate the results obtained in this research you must have:

1. Compilers:

   This project heavily relies on [Verificarlo version 1.0.0](https://github.com/verificarlo). I advise you to check the documentation.
   
   On Kebnekaise, we use g++ version 10.2, on Laptop we use g++ version 11.4.0.

   Both with Verificarlo and GNU Compilers, everything is compiled with -O2 optimization flag.
   
   
2. Use Cases:
   The LULESH use case is using [version 2.0](https://github.com/LLNL/LULESH). And more information about LULESH is available [here](https://asc.llnl.gov/codes/proxy-apps/lulesh).

   Detailed information on the Reactor Simulator and the code is available in [here](https://people.math.sc.edu/Burkardt/cpp_src/reactor_simulation/reactor_simulation.html), C++ version is used in our experiments.

3. Reproducing Graphs:
   We used Python ... and related packages... to produce the graphs and analyze the results.
   Remember: reporducing *exactly* the same results as in this study is a challange. But if you want to try anyway, detailed information about the systems is given in the internship report.
   
## Key Findings:
Through case studies on the Reactor Simulator and LULESH benchmarks, we demonstrated
that applying mixed-precision strategies can lead to significant reductions in both time-to-
solution and energy-to-solution, sometimes without sacrificing accuracy. Our findings show a
15% reduction in both metrics without any compromise on accuracy, for the Reactor Simulator
and up to a 20% improvement in time-to-solution and a 10% reduction in energy-to-solution
for the LULESH benchmark. These results highlight the importance of adopting ‘just enough
precision’ to optimize performance and energy use in scientific computing.

## Contact :
If you have any questions, or want to let us know about your reuslts please do not hesitate to contact at this mail:
ggedik@cs.umu.se