format long

disp('Questão 1')
disp('')

x = [1.0 2.1 3.0 3.9 5.0 6.0 7.2 8.1 9.2 10.4];
y = [1.5 0.1 -0.4 0.2 1.7 2.2 1.6 0.4 -0.4 0.5];
n = 8;

xp = min(x) : 1/100 : max(x);

a1 = fCalculaCoefAjustePn(x, y, n);
yp1 = fPn(n, a1, xp);
desvioModuloPn = sum(abs(fPn(n, a1, x).-y))/length(x)

a2 = fCalculaCoefAjustegx1(x, y);
yp2 = fgx1(a2, xp);
desvioModulogx1 = sum(abs(fgx1(a2, x).-y))/length(x)

a3 = fCalculaCoefAjustegx2(x, y);
yp3 = fgx2(a3, xp);
desvioModulogx3 = sum(abs(fgx2(a3, x).-y))/length(x)

plt = plot(
    x, y, '*k',
    xp, yp1, '-r',
    xp, yp2, '-b',
    xp, yp3, '-g'
);
legend(
    'Pontos originais',
    'Polinomial',
    'Combinação de seno e cosseno',
    'Cosseno deslocado'
);

disp('')
disp('A aproximação de melhor qualidade foi a Polinomial, porque resultou nos menores desvios.')

disp('')
disp('')
disp('Questão 2')
disp('')

x = -3 : 1/10 : 3;

yerf = erf(x);

for i = 1:length(x)
    temp = erf2(x(i));

    ytrapezios(i) = temp(1);
    ygauss(i) = temp(2);
    ysimpson(i) = temp(3);
end

erroTrapezios = max(abs(yerf - ytrapezios))
erroGauss = max(abs(yerf - ygauss))
erroSimpson = max(abs(yerf - ysimpson))
