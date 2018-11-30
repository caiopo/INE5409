format long

f = @(x) log(x);

a = 0.01;
b = 1;

disp('Questão 3')

n = 2**18;
Tn = fIntegralTrapezios(n, a, b, f)
erroExatoEstimadoTn = abs(Tn - fIntegralTrapezios(2*n, a, b, f))

disp('')
disp('')
disp('Questão 4')

n = 2**11;
Sn = fIntegralSimpson(n, a, b, f)
erroExatoEstimadoSn = abs(Sn - fIntegralSimpson(2*n, a, b, f))

disp('')
disp('')
disp('Questão 5')

m = 22;
Gm = fIntegralGauss(m, a, b, f)
erroExatoEstimadoGm = abs(Gm - fIntegralGauss(m+1, a, b, f))

disp('')
disp('')
disp('Questão 7')

m = 1e3;
GTmExato = 1/pi * 2.4039394306344129982733248925915; % retirado do wolfram

GTm = 1/pi * fGTm(m)

erroGTm = abs(GTmExato - GTm)

disp('')
disp('')
disp('Questão 8')

x = [1 2 4 7 11 17 23 29 35 41];
y = [4.3 3.9 3.3 2.9 2.5 2.1 1.8 1.5 1.4 1.2];

xp = min(x) : 1/100 : max(x);

n = 4;
a1 = fCalculaCoefAjustePn(x, y, n)
yp1 = fPn(n, a1, xp);

disp('')
disp('')
disp('Questão 9')

desviosPn = (fPn(n, a1, x) .- y).^2

plt = plot(
    x, y, '*k',
    xp, yp1, '-r'
);
legend(
    'Pontos originais',
    'Ajuste polinomial'
)
waitfor(plt)
