format long

a = -1;
b = 1;

x = -1 : 1/10 : 1;

[ygreg ymaclaurin ytcheb ypade] = faprox(a,b,x);

yexato = f(x);

disp('Calculando log(x) para x em [1, 10] chegamos aos seguintes erros:')

disp('')
errogreg = max(abs(yexato - ygreg))
erromaclaurin = max(abs(yexato - ymaclaurin))
errotcheb = max(abs(yexato - ytcheb))
erropade = max(abs(yexato - ypade))

disp('')
disp('A aproximação computacionalmente mais eficiente foi Padé (n = 6, m = 5)')

