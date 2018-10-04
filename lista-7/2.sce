// Import the diagram and set the ending time
loadScicos();
loadXcosLibs();
importXcosDiagram("SCI/modules/xcos/examples/solvers/ODE_Example.zcos");
scs_m.props.tf = 5000;

// Select the solver Runge-Kutta and set the precision
scs_m.props.tol(6) = 6;
scs_m.props.tol(7) = 10^-2;

// Start the timer, launch the simulation and display time
tic();
try xcos_simulate(scs_m, 4); catch disp(lasterror()); end
t = toc();
disp(t, "Time for Runge-Kutta:");
