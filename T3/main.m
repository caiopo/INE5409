format long

a = 0;
b = pi/2;
np = 100;
x = -1 : (b-a)/np : 1;

y_exato = f(x, a, b);

disp('Interpolação polinomial')
n_interp = 5
x_interp = -1 : 2/n_interp : 1;
coef_interp = fcoefinterPn(n_interp,x_interp,f(x_interp, a,b))
y_interp =fPnH(n_interp,coef_interp,x);
erro_interp = abs(y_interp-y_exato);
erro_max_interp = max(erro_interp)

disp('')
disp('')
disp('Maclaurin')
n_maclaurin = 6
coef_maclaurin = fCoefMaclaurin(n_maclaurin,a,b)
y_maclaurin = fPnH(n_maclaurin, coef_maclaurin, x);
erro_maclaurin = abs(y_maclaurin-y_exato);
erro_max_maclaurin = max(erro_maclaurin)

disp('')
disp('')
disp('Tchebychev')
n_tcheb = 5
ytc = fTchebychev(n_tcheb, a, b)
y_tcheb = fCalculaTchebychev(n_tcheb, ytc, x);
erro_tcheb = abs(y_tcheb-y_exato);
erro_max_tcheb = max(erro_tcheb)

disp('')
disp('')
disp('Padé')
n_pade = 3
m_pade = 3
y_pade = fPnPade(n_pade, m_pade, x);
erro_pade = abs(y_pade-y_exato);
erro_max_pade = max(erro_pade)

plot(
    x, erro_interp, 'r',
    x, erro_maclaurin, 'g',
    x, erro_tcheb, 'y',
    x, erro_pade, 'b'
);
grid on;
legend('Interpolação polinomial', 'Maclaurin', 'Tchebychev', 'Padé');
waitfor(plt);
