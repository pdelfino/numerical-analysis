function z = f(t,y)
    //f(t,z) represents the sysmte of ODEs:
    //    -the first argument should always be the independe variable
    //    -the second argument should always be the dependent variables
    //    -it may have more than two arguments
    //    -y is a vector 2x1: y(1) = theta, y(2) = theta'
    //    -z is a vector 2x1: z(1) = z    , z(2) = z'

    z(1) = y(2)         //first equation:  z  = theta'
    z(2) = 10*sin(y(1)) //second equation: z' = 10*sin(theta)
endfunction

ts = linspace(0,3,200);
theta0  = %pi/4;
dtheta0 = 0;
y0 = [theta0; dtheta0];
t0 = 0;
thetas = ode('rk',y0, t0, ts, 0.1, f); //the output have the same order
                                  //as the argument `y` of f()

scf(1); clf();
plot2d(thetas(2,:),thetas(1,:),-5);
xtitle('Phase portrait', 'theta''(t)','theta(t)');
xgrid();
