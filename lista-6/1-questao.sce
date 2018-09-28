
function E=euler(f,a,b,ya,M)
h=(b-a)/M;
Y=zeros(1,M+1);
T=a:h:b;
Y(1)=ya;
for j=1:M
    Y(j+1)=Y(j)+h*f(T(j));
end
E=[T' Y'];
end

function output=f(x)
    output = x^2;
endfunction

a=0;
b=10;
ya=0;
M=200;
YY=euler(f,a,b,ya,M);
