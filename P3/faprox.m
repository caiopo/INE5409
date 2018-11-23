function [ygreg ymaclaurin ytcheb ypade] = faprox(a, b, x)
    ngreg = 20;
    xgreg = a : (b-a)/ngreg : b;
    yexato = f(x);

    difdiv1 = fdifdiv(ngreg, xgreg, yexato);
    ygreg = fgregoryn(ngreg, xgreg, yexato, difdiv1, x);

    nmac = 50;
    cmac = fcoefMaclaurin(nmac,a,b);
    ymaclaurin = fPnH(nmac, cmac, x);

    ntcheb = 12;
    ytc = fTchebychev(ntcheb, 1, 10);
    ytcheb = fcalculaTchebychev(ntcheb, ytc, x);

    npade = 6;
    mpade = 6;
    ypade = fPnPade(npade, mpade, x);
end

