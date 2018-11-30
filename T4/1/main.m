x=[ 1.0 2.1 3.0 3.9 5.0 6.0  7.2 8.1  9.2 10.4];
y=[ 1.5 0.1 -0.4 0.2 1.7 2.2 1.6  0.4 -0.4  0.5 ];

xp = min(x):0.01:max(x);
% ajuste para g(x) = a(1)*sen(x) + a(2)*cos(x)
a1 = fCalculaCoefAjustegx1(x, y);
DesvioModulogx1 = sum(abs(fgx1(a1, x).-y))/length(x)
yp2 = fgx1(a1, xp);

disp("Os pontos são bem proximos com o formato da f1, o que levar a modifcar a amplitude para a função 2.")

#a = [ rand * 10  rand * 10  rand * 10  rand * 10  rand * 10  rand * 10]
a = [2 1 1 1.2 1 1 1]
yTest = fgx2(a, x);
#testeDeZero = fFa(a, x , yTest)
aNewton = fNewtonSistemasNaoLineares(a, 0.001, x, y)
yp3 = fgx2(aNewton, xp);
plt=plot(x, y, '*', 16, 0, xp, yp2, '-b', xp, yp3, '-g');

a1

waitfor(plt);
