%shooting method
clear
clc
format long
a=0  % Valor inicial de x
b=1  % Valor final de x do cominio de calculo
% Condição Inicial:
t(1) =a  % Valor inicial de x
y1(1)=0; % Valor inicial de y1
%y2(1)=?; % Valor inicial (C.I.) de y2 "desconhecido" =C
%y1(n+1)=9.389056098930666 % Valor final(C.C.) de y1 "conhecido" =D
D=9.389056098930666
%RK4 p/ sistemas de 2 EDOs
tolerancia=1e-6;%erro maximo 1e-6
%Vamos estabelecer o n mínimo praa que a solução y1 tenha erromaximo<tolerancia
n=18  % Numero de subdivisões do intervalor [a,b] para que o Erro<1e-6 (por tentativas)

%% pode-se aplicar um algoritmo de Newton para deternimar C na eq. 
% f(C)=D2(C)-D
C=fcalculaC2(n,a,b,t,y1,D,tolerancia) %shooting method
y2(1)=C;%ultimo valor calculado de C é o correto p/ y2(1), mas ainda depende de n. 
[t y1 y2]=fRK4sist2(n,a,b,t,y1,y2);
ye=2.*t.*t.+t.*exp(2.*t);%Valor exato p/ comparação
erroexatomax1=max(abs(y1.-ye)) %Erro exato maximo em todo o dominio de t (para aferição)
[ta y1a y2a]=fRK4sist2(2*n,a,b,t,y1,y2); %valor mais proximo dom exato
erroestimmax2=abs(y1(n/2+1)-y1a(n+1)) %Erro estimado no meio intervalo.
%% algoritmo de busca opcional

plot(t,ye,'*',t,y1,'r')
