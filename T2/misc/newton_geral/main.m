f = @(x) x .* tan(x) .- 1;
init=0
final=3*pi

Xi=fLocalizaRaiz(f,init,final) % localiza todas as raizaes iniciais no intervalo [init; final]

for k=1:length(Xi)
    %newton(f, Xi(k), 1e-4) %precisa do arquivo p/ df(x) - derivada
    X(k)=fNewtonNum(f, Xi(k), 1e-15); %nao precisa da derivada
    residuosf(k)=abs(f(X(k)));
end
X
residuosf
