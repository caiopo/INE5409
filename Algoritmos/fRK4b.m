function [x y]=fRK4(n,a,b,x,y)
h=(b-a)/n; % espacamento em x
for k=1:n
    K1f=f11(x(k),      y(k)          );
    K2f=f11(x(k)+0.5*h,y(k)+0.5*h*K1f);
    K3f=f11(x(k)+0.5*h,y(k)+0.5*h*K2f);
    K4f=f11(x(k)+h,    y(k)+    h*K3f);
    x(k+1)=x(k)+h;
    y(k+1)=y(k)+(h/6)*(K1f+2*(K2f+K3f)+K4f);
end
end