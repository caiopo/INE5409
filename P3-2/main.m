format long

a = -1;
b = 1;

x = -1 : 1/100 : 1;

[ygreg ymaclaurin ytcheb ypade] = faprox(a,b,x);

yexato = f(x);

disp('Calculando sin(x) para x em [0, pi/2] chegamos aos seguintes erros:')

disp('')
errogreg = abs(yexato - ygreg);
erromaclaurin = abs(yexato - ymaclaurin);
errotcheb = abs(yexato - ytcheb);
erropade = abs(yexato - ypade);

erromaxgreg = max(errogreg)
erromaxmaclaurin = max(erromaclaurin)
erromaxtcheb = max(errotcheb)
erromaxpade = max(erropade)

disp('')
disp('A aproximação computacionalmente mais eficiente foi Padé (n = 8, m = 8)')


plt = plot(
    x, errogreg, 'b',
    x, erromaclaurin, 'g',
    x, errotcheb, 'r',
    x, erropade, 'k'
);

legend(
    'Erro Gregory-Newton',
    'Erro Maclaurin',
    'Erro Tchebychev',
    'Erro Padé'
);

waitfor(plt);
