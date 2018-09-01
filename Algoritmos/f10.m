function D1=f10(n,a,b,x,y1,y2,C1,D)
y3(1)=C1; % Valor inicial de y2 "desconhecido", atribuido
[x y1 y2 y3]=fsis3RK4(n,a,b,x,y1,y2,y3);
%y2(n+1) correto é D
D1=y2(n+1)-D; %f(C)=D1-D
end