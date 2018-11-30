format long
x = [ 1.0 2.1  3.0 3.9 5.0 6.0  7.2 8.1  9.2 10.4];
y = [ 1.5 0.1 -0.4 0.2 1.7 2.2 1.6  0.4 -0.4  0.5 ];
n = 9;

% ajuste polinomial
a = fCalculaCoefAjustePn(x, y, n);
a = fliplr(polyfit(x, y, n));

xp = min(x):0.01:max(x);
yp = fPn(n, a, xp);

DesvioModuloPn = sum(abs(fPn(n, a, x).-y))/length(x);

% ajuste para g(x) = a(1)*sen(x) + a(2)*cos(x)
a2 = fCalculaCoefAjustegx1(x, y);

yp2 = fgx1(a2, xp);

DesvioModulogx1 = sum(abs(fgx1(a2, x).-y))/length(x);

% plot(xp, yp,'-r', x, y, '*', 16, 0, xp, yp2, '-b');

x = 1;
Ve = erf(x)
Va = erf2(x)
printf('Erros: ');
erros = abs(Ve .- Va)	 	  	 	      	      	 	     	    	     	      	 	
