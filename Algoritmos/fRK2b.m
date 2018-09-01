function [x y]=fRK2(n,a,b,x,y)
h=(b-a)/n; % espacamento em x
for k=1:n
    K1f=f11(x(k)  ,y(k)      );
    K2f=f11(x(k)+h,y(k)+h*K1f);
    x(k+1)=x(k)+h;
    y(k+1)=y(k)+(h/2)*(K1f+K2f);
end
end