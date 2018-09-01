function D1=f9(n,a,b,t,y1,C1,D)
y2(1)=C1; % Valor inicial de y2 "desconhecido", atribuido
[t y1 y2]=fRK4sist2(n,a,b,t,y1,y2);
D1=y1(n+1)-D; %f(C)=D1-D
end