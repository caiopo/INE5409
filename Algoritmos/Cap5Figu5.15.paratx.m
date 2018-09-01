% Represente uma funcao parametrizada em t
a=-1 %valor inicial do intervalo
b=+1. %valor final do intervalo
m=2^8 %numero de subdivicoes do intervalo [a ; b] para m+1 pontos
t=a:(b-a)/m:b; %variavel auxiliar
x=1.+t.-(t).^2.-1.2.*(t).^3; 
y=1.+t.-(t).^2; 
plot(x,y,'-k','linewidth',2)
grid