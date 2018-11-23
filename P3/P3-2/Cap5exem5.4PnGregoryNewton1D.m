%Algoritmo Interpolador Polinomial Geral (via sistema de eqs. Lineares):
%Cálculo do erro exato de interpolação = |Pn(x)-f(x)|
clear
clc
format long
a = 1;
b = 10;
n = 10;
h = (b-a)/n;
x = a : h : b;
y = f(x);
difdiv1=fdifdiv(n,x,y);

%Plotagem e calculo do erro exato:
np = 100; %numero de intervalos para plotar grafico
hp = (b-a)/np;
xp = a:hp:b;
ye = f(xp);

size(n)
size(x)
size(y)
size(difdiv1)
size(xp)

yintp = fgregoryn(n,x,y,difdiv1,xp);
erro  = abs(yintp - ye);
ErroMax=max(erro);

plt = plot(x,y,'*k','markersize',20,xp,ye,'--k','LineWidth',1,xp,yintp,'-k','LineWidth',2);
legend('f(x) tabelada','f(x)=ln(x) exata','P2(x) interpolador','location','north')
waitfor(plt);
grid on
