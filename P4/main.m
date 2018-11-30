format long

f = @(x) log(x);

a = 0.01;
b = 1;

disp('')
disp('Questão 3')

n = 2**18;
Tn = fIntegralTrapezios(n, a, b, f)
erroExatoEstimadoTn = abs(Tn - fIntegralTrapezios(2*n, a, b, f))

disp('')
disp('Questão 4')

n = 2**11;
Sn = fIntegralSimpson(n, a, b, f)
erroExatoEstimadoSn = abs(Sn - fIntegralSimpson(2*n, a, b, f))


disp('')
disp('Questão 5')

m = 22;
Gm = fIntegralGauss(m, a, b, f)
erroExatoEstimadoGm = abs(Gm - fIntegralGauss(m+1, a, b, f))
